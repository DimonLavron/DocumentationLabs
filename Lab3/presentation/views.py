# from bussiness_logic.controllers import RideController
# from main import app
# from flask import jsonify, make_response, request
# from models import db

# from data_access.managers import RideManager

# ride_manager = RideManager(db.session)
# ride_controller = RideController(ride_manager)

# @app.route('/request', methods=['GET'])
# def get_records():
#     with app.app_context():
#         return jsonify(repr(ride_controller.get_all_objects())), 200


# @app.route('/request/<string:id>', methods=['GET'])
# def get_record_by_id(id):
#     with app.app_context():
#         if not ride_controller.get_object_by_id(id):
#             abort(404)
#         return jsonify(repr(ride_controller.get_object_by_id(id))), 200


# @app.route('/request', methods=['POST'])
# def create_record():
#     if not request.get_json():
#         abort(400)

#     data = request.get_json(force=True)

#     if not data.get('departure_address') or not data.get('destination_address') or not data.get('price') or not data.get('customer') or not data.get('driver'):
#         abort(400)
#     with app.app_context():
#         ride_controller.create_object(departure_address=data.get('departure_address'), destination_address=data.get('destination_address'), price=data.get('price'), customer=data.get('customer'), driver=data.get('driver'))
#         db.session.commit()
#     return '', 201


# @app.route('/request/<string:id>', methods=['PUT'])
# def edit_record(id):
#     with app.app_context():
#         if not ride_controller.get_object_by_id(id):
#             abort(404)

#         if not request.get_json():
#             abort(400)
#         data = request.get_json(force=True)

#         if not data.get('departure_address') or not data.get('destination_address') or not data.get('price') or not data.get('customer') or not data.get('driver'):
#             abort(400)
#         ride_controller.update_object(id, data.get('departure_address', None), 
#                                                 data.get('destination_address', None), data.get('price', None), data.get('customer', None), data.get('driver', None))
#         db.session.commit()
#         return jsonify(repr(ride_controller.get_product_by_id(id))), 200


# @app.route('/request/<string:id>', methods=['DELETE'])
# def delete_record(id):
#     with app.app_context():
#         if not ride_controller.get_object_by_id(id):
#             abort(404)

#         ride_controller.delete_object(id)
#         db.session.commit()

#     return '', 204
