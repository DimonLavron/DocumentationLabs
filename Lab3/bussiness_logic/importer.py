import csv_processor


class Importer:
    def __init__(self, customer_manager, driver_manager, ride_manager):
        self.customer_manager = customer_manager
        self.driver_manager = driver_manager
        self.ride_manager = ride_manager

    def import_csv_data(self):
        parsed_csv = csv_processor.parse_csv()
        customer_fields, customer_data = parsed_csv['customer']
        driver_fields, driver_data = parsed_csv['driver']
        ride_fields, ride_data = parsed_csv['ride']

        for customer in customer_data:
            self.customer_manager.csv_import(
                customer_fields, customer)
    
        for driver in driver_data:
            self.driver_manager.csv_import(
                driver_fields, driver)
        
        for ride in ride_data:
            self.ride_manager.csv_import(
                ride_fields, ride)
        