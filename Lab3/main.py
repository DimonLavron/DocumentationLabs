from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from bussiness_logic.importer import Importer
from data_access.managers import (
    CustomerManager,
    DriverManager,
    RideManager,
)
from bussiness_logic.controllers import RideController
from models import db

from csv_processor import generate_csv_with_data

from flask import Flask, jsonify, abort, request
from flask_swagger_ui import get_swaggerui_blueprint


app = Flask(__name__)

# from presentation import views

DB_PATH = 'uklon.db'


def main():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + DB_PATH
    db.init_app(app)
    with app.app_context():
        generate_csv_with_data()
        db.drop_all()
        db.create_all()
        customer_manager = CustomerManager(db.session)
        driver_manager = DriverManager(db.session)
        ride_manager = RideManager(db.session)
        
        importer = Importer(customer_manager, driver_manager, ride_manager)

        ride_controller = RideController(ride_manager)

        importer.import_csv_data()
        db.session.commit()

        SWAGGER_URL = '/swagger'
        API_URL = '/static/swagger.json'
        SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
            SWAGGER_URL,
            API_URL,
            config={
                'app_name': "Lab3"
            }
        )
        app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

        @app.route('/request', methods=['GET'])
        def get_rides():
            with app.app_context():
                return jsonify(repr(ride_controller.get_all_objects())), 200


        @app.route('/request/<string:id>', methods=['GET'])
        def get_ride_by_id(id):
            with app.app_context():
                if not ride_controller.get_object_by_id(id):
                    abort(404)
                return jsonify(repr(ride_controller.get_object_by_id(id))), 200


        @app.route('/request', methods=['POST'])
        def create_ride():
            if not request.get_json():
                abort(400)

            data = request.get_json(force=True)

            if not data.get('departure_address') or not data.get('destination_address') or not data.get('price') or not data.get('customer') or not data.get('driver'):
                abort(400)
            with app.app_context():
                ride_controller.create_object(departure_address=data.get('departure_address'), destination_address=data.get('destination_address'), price=data.get('price'), customer=data.get('customer'), driver=data.get('driver'))
                db.session.commit()
            return '', 201


        @app.route('/request/<string:id>', methods=['PUT'])
        def update_ride(id):
            with app.app_context():
                if not ride_controller.get_object_by_id(id):
                    abort(404)

                if not request.get_json():
                    abort(400)
                data = request.get_json(force=True)

                if not data.get('departure_address') or not data.get('destination_address') or not data.get('price') or not data.get('customer') or not data.get('driver'):
                    abort(400)
                ride_controller.update_object(id, data.get('departure_address', None), 
                                                        data.get('destination_address', None), data.get('price', None), data.get('customer', None), data.get('driver', None))
                db.session.commit()
                return jsonify(repr(ride_controller.get_object_by_id(id))), 200


        @app.route('/request/<string:id>', methods=['DELETE'])
        def delete_ride(id):
            with app.app_context():
                if not ride_controller.get_object_by_id(id):
                    abort(404)

                ride_controller.delete_object(id)
                db.session.commit()

            return '', 204

        app.run()


if __name__ == '__main__':
    main()