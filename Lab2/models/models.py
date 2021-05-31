from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    phone_number = Column(String)
    rate = Column(Float)
    ride_quantity = Column(Integer)

class Customer(User):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, ForeignKey('user.email'))
    home_address = Column(String)
    work_address = Column(String)

    def csv(self, fields, values):
        fields_list = fields.split(',')
        values_list = values.split(',')

        for column, value in zip(fields_list, values_list):
            if hasattr(self, column):
                setattr(self, column, value)

class Driver(User):
    __tablename__ = 'driver'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, ForeignKey('user.email'))
    car_class = Column(String)
    available = Column(Boolean)
    services = Column(String)

    def csv(self, fields, values):
        fields_list = fields.split(',')
        values_list = values.split(',')

        for column, value in zip(fields_list, values_list):
            if hasattr(self, column):
                setattr(self, column, value)

class Ride(Base):
    __tablename__ = 'ride'

    id = Column(Integer, primary_key=True, autoincrement=True)
    departure_address = Column(String)
    destination_address = Column(String)
    price = Column(Integer)
    start_date_time = Column(DateTime)
    end_date_time = Column(DateTime)
    services = Column(String)
    customer = Column(Integer, ForeignKey('customer.id'))
    driver = Column(Integer, ForeignKey('driver.id'))

    def csv(self, fields, values):
        fields_list = fields.split(',')
        values_list = values.split(',')

        for column, value in zip(fields_list, values_list):
            if hasattr(self, column):
                setattr(self, column, value)
