from models.models import Customer, Driver, Ride

class CustomerManager:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Customer).all()
    
    def get(self, customer_id):
        return self.session.query(Customer).filter_by(id=customer_id).first()
    
    def post(self, email, first_name, last_name, phone_number, home_address, work_address):
        new_customer = Customer()
        new_customer.email = email
        new_customer.first_name = first_name
        new_customer.last_name = last_name
        new_customer.phone_number = phone_number
        new_customer.home_address = home_address
        new_customer.work_address = work_address
        self.session.add(new_customer)
    
    def delete(self, customer_id):
        customer = self.get(customer_id)
        if customer:
            self.session.delete(customer)

    def csv_import(self, customer_fields, customer_data):
        customer = Customer()
        customer.csv(customer_fields, customer_data)
        self.session.add(customer)

class DriverManager:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Driver).all()
    
    def get(self, driver_id):
        return self.session.query(Driver).filter_by(id=driver_id).first()
    
    def post(self, email, first_name, last_name, phone_number, car_class, services):
        new_driver = Driver()
        new_driver.email = email
        new_driver.first_name = first_name
        new_driver.last_name = last_name
        new_driver.phone_number = phone_number
        new_driver.car_class = car_class
        new_driver.services = services
        self.session.add(new_driver)
    
    def delete(self, driver_id):
        driver = self.get(driver_id)
        if driver:
            self.session.delete(driver)

    def csv_import(self, driver_fields, driver_data):
        driver = Driver()
        driver.csv(driver_fields, driver_data)
        self.session.add(driver)

class RideManager:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Ride).all()
    
    def get(self, ride_id):
        return self.session.query(Ride).filter_by(id=ride_id).first()
    
    def post(self, departure_address, destination_address, price, customer, driver):
        new_ride = Ride()
        new_ride.departure_address = departure_address
        new_ride.destination_address = destination_address
        new_ride.price = price
        new_ride.customer = customer
        new_ride.driver = driver
        self.session.add(new_ride)
    
    def put(self, id, departure_address=None, destination_address=None, price=None, customer=None, driver=None):
        ride = self.get(id)
        self.session.delete(ride)
        if not departure_address is None:
            ride.departure_address = departure_address
        if not destination_address is None:
            ride.destination_address = destination_address
        if not price is None:
            ride.price = price
        if not customer is None:
            ride.customer = customer
        if not driver is None:
            ride.driver = driver
        self.session.add(ride)

    
    def delete(self, ride_id):
        ride = self.get(ride_id)
        if ride:
            self.session.delete(ride)

    def csv_import(self, ride_fields, ride_data):
        ride = Ride()
        ride.csv(ride_fields, ride_data)
        self.session.add(ride)
