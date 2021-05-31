import random
import string

table_names = ['customer', 'driver', 'ride']

first_names = [
    'Mark', 'Amber', 'Todd', 'Anita', 'Sandy',
    'John', 'Fred', 'Jason', 'Keyser', 'Lily',
    'Anna', 'Mike', 'Luke', 'Andrea', 'Lisa',
    'Stephen', 'James', 'Albert', 'Emma', 'Lia',
]
last_names = [
    'Silva', 'Hughes', 'Obrien', 'Barron', 'Cook', 'Booth', 
    'Mckay', 'Case', 'Sanford', 'Deleon', 'Tate', 'Armstrong'
]

def generate_csv_with_data(filename='import_data.csv', entries=400):
    customer_fields = 'email,first_name,last_name,phone_number,home_address,work_address\n'
    data_list = []
    for i in range(1, entries + 1):
        email = ''.join(random.choices(string.ascii_lowercase + string.digits,
                                       k=random.randint(4, 8))) + '@gmail.com'
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        phone_number = ''.join(random.choices(string.digits, k=8))
        home_address = ''.join(random.choices(string.ascii_lowercase,
                                         k=random.randint(4, 12))).title()
        work_address = ''.join(random.choices(string.ascii_lowercase,
                                         k=random.randint(4, 12))).title()
        data_list.append(','.join([email, first_name, last_name, phone_number, home_address, work_address]) + '\n')
    with open(filename, 'w') as file:
        file.write('CUSTOMER\n')
        file.write(customer_fields)
        file.writelines(data_list)

    driver_fields = 'email,first_name,last_name,phone_number,car_class,services\n'
    data_list = []
    for i in range(1, entries + 1):
        email = ''.join(random.choices(string.ascii_lowercase + string.digits,
                                       k=random.randint(4, 8))) + '@gmail.com'
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        phone_number = ''.join(random.choices(string.digits, k=8))
        car_class = ''.join(random.choices(string.ascii_lowercase,
                                         k=random.randint(4, 12))).title()
        services = ''.join(random.choices(string.ascii_lowercase,
                                         k=random.randint(4, 12))).title()
        data_list.append(','.join([email, first_name, last_name, phone_number, car_class, services]) + '\n')
    with open(filename, 'a') as file:
        file.write('DRIVER\n')
        file.write(driver_fields)
        file.writelines(data_list)

    ride_fields = 'departure_address,destination_address,price,customer,driver\n'
    data_list = []
    for i in range(1, entries + 1):
        departure_address = ''.join(random.choices(string.ascii_lowercase,
                                         k=random.randint(4, 12))).title()
        destination_address = ''.join(random.choices(string.ascii_lowercase,
                                         k=random.randint(4, 12))).title()
        price = ''.join(random.choices(string.digits, k=2))
        customer = str(random.randint(1, 400))
        driver = str(random.randint(1, 400))
        data_list.append(','.join([departure_address, destination_address, price, customer, driver]) + '\n')
    with open(filename, 'a') as file:
        file.write('RIDE\n')
        file.write(ride_fields)
        file.writelines(data_list)
    
def parse_csv(filename='import_data.csv'):
    with open(filename, 'r') as file:
        lines = file.readlines()
    lines = [line[:-1] for line in lines if line.endswith('\n')]

    customer_table = lines.index('CUSTOMER')
    customer_fields = lines[customer_table + 1]

    driver_table = lines.index('DRIVER')
    driver_fields = lines[driver_table + 1]

    ride_table = lines.index('RIDE')
    ride_fields = lines[ride_table + 1]

    customer_list = lines[customer_table + 2 : driver_table]
    driver_list = lines[driver_table + 2 : ride_table]
    ride_list = lines[ride_table + 2 :]

    return {
        'customer': (customer_fields, customer_list),
        'driver': (driver_fields, driver_list),
        'ride': (ride_fields, ride_list),
    }