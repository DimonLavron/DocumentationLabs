from . import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    phone_number = db.Column(db.String)
    rate = db.Column(db.Float)
    ride_quantity = db.Column(db.Integer)

class Customer(User):
    __tablename__ = 'customer'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, db.ForeignKey('user.email'))
    home_address = db.Column(db.String)
    work_address = db.Column(db.String)

    def csv(self, fields, values):
        fields_list = fields.split(',')
        values_list = values.split(',')

        for column, value in zip(fields_list, values_list):
            if hasattr(self, column):
                setattr(self, column, value)

class Driver(User):
    __tablename__ = 'driver'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, db.ForeignKey('user.email'))
    car_class = db.Column(db.String)
    available = db.Column(db.Boolean)
    services = db.Column(db.String)

    def csv(self, fields, values):
        fields_list = fields.split(',')
        values_list = values.split(',')

        for column, value in zip(fields_list, values_list):
            if hasattr(self, column):
                setattr(self, column, value)

class Ride(db.Model):
    __tablename__ = 'ride'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    departure_address = db.Column(db.String)
    destination_address = db.Column(db.String)
    price = db.Column(db.Integer)
    start_date_time = db.Column(db.DateTime)
    end_date_time = db.Column(db.DateTime)
    services = db.Column(db.String)
    customer = db.Column(db.Integer, db.ForeignKey('customer.id'))
    driver = db.Column(db.Integer, db.ForeignKey('driver.id'))

    def csv(self, fields, values):
        fields_list = fields.split(',')
        values_list = values.split(',')

        for column, value in zip(fields_list, values_list):
            if hasattr(self, column):
                setattr(self, column, value)
    
    def __repr__(self):
        string = f'Ride: '
        if hasattr(self, 'id'):
            string += f'id:{self.id}, '
        string += f'departure_address:{self.departure_address}, destination_address:{self.destination_address}, price:{self.price}, customer:{self.customer}, driver:{self.driver}'
        return string
