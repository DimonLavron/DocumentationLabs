from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from bussiness_logic.controllers import (
    CustomerController,
    DriverController,
    RideController
)
from bussiness_logic.importer import Importer
from data_access.managers import (
    CustomerManager,
    DriverManager,
    RideManager,
)
from models.models import Base

from csv_processor import generate_csv_with_data


DB_PATH = 'uklon.db'


def main():
    generate_csv_with_data()
    engine = create_engine('sqlite:///' + DB_PATH)
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)

    with Session() as session:
        customer_manager = CustomerManager(session)
        driver_manager = DriverManager(session)
        ride_manager = RideManager(session)
        
        customer_controller = CustomerController(customer_manager)
        driver_controller = DriverController(driver_manager)
        ride_controller = RideController(ride_manager)
        
        importer = Importer(customer_manager, driver_manager, ride_manager)

        importer.import_csv_data()
        session.commit()

        print('CUSTOMERS')
        for customer in customer_controller.get_all_objects()[:5]:
            print(customer.first_name, customer.last_name)

        print('DRIVERS')
        for driver in driver_controller.get_all_objects()[:5]:
            print(driver.first_name, driver.last_name)

        print('RIDES')
        for ride in ride_controller.get_all_objects()[:5]:
            print(ride.departure_address, ride.destination_address)


if __name__ == '__main__':
    main()