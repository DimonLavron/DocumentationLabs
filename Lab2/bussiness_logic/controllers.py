from data_access.managers import CustomerManager, DriverManager, RideManager

class CustomerController:
    def __init__(self, manager):
        self.manager = manager

    def get_all_objects(self):
        return self.manager.get_all()

    def get_object_by_id(self, customer_id):
        return self.manager.get(customer_id)

    def create_object(self, email, first_name, last_name, phone_number, home_address, work_address):
        return self.manager.post(email, first_name, last_name, phone_number, home_address, work_address)

    def delete_object(self, customer_id):
        return self.manager.delete(customer_id)

class DriverController:
    def __init__(self, manager):
        self.manager = manager

    def get_all_objects(self):
        return self.manager.get_all()

    def get_object_by_id(self, driver_id):
        return self.manager.get(driver_id)

    def create_object(self, first_name, last_name, phone_number, car_class, services):
        return self.manager.post(first_name, last_name, phone_number, car_class, services)

    def delete_object(self, driver_id):
        return self.manager.delete(driver_id)

class RideController:
    def __init__(self, manager):
        self.manager = manager

    def get_all_objects(self):
        return self.manager.get_all()

    def get_object_by_id(self, ride_id):
        return self.manager.get(ride_id)

    def create_object(self, departure_address, destination_address, price, customer, driver):
        return self.manager.post(departure_address, destination_address, price, customer, driver)

    def delete_object(self, ride_id):
        return self.manager.delete(ride_id)
