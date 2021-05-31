from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster
from ssl import PROTOCOL_TLSv1_2, CERT_NONE, SSLContext
from src import cql
import redis
import config


class ConsoleOutputStrategy():
    def process_data(self, data):
        if data is dict:
            data = [data]
        for entry in data:
            print(entry)


class CosmosDBSavingStrategy():
    def __init__(self):
        ssl_context = SSLContext(PROTOCOL_TLSv1_2)
        ssl_context.verify_mode = CERT_NONE

        auth_provider = PlainTextAuthProvider(
            username=config.COSMOS_DB_USERNAME,
            password=config.COSMOS_DB_PASSWORD)
        self.cluster = Cluster([config.COSMOS_DB_CONTACT_POINT], port=config.COSMOS_DB_PORT,
                               auth_provider=auth_provider, ssl_context=ssl_context)
        self.session = self.cluster.connect(config.COSMOS_DB_KEYSPACE)
        self.session.execute(cql.DELETE_TABLE_SCRIPT)
        self.session.execute(cql.CREATE_TABLE_SCRIPT)

    def process_data(self, data):
        if data is dict:
            data = [data]
        for record in data:
            self.session.execute(cql.INSERT_DATA_SCRIPT.format(**record))


class ConsoleLoggingStrategy():
    def get_status(self, resourse_name):
        pass

    def get_logged_rows_number(self):
        return 0

    def log_start(self, resource_name):
        print(f'{resource_name} - START')

    def log_completed(self, resource_name):
        print(f'{resource_name} - COMPLETED')

    def log_progress(self, resource_name, data_range):
        start, end = data_range
        print(f'Rows: {start}-{end}\t(from {resource_name})')

    def log_already_exists(self, resource_name):
        print(f'{resource_name} ignored. Data already exists!')


class RedisLoggingStrategy():
    def __init__(self):
        self.redis_connector = redis.StrictRedis(
            host=config.REDIS_HOSTNAME,
            port=config.REDIS_PORT,
            password=config.REDIS_KEY,
            ssl=True)
        is_working = self.redis_connector.ping()
        if not is_working:
            print('Redis connection failed!')
        else:
            print('Successfully connected to Redis.')

    def get_status(self, resource_name):
        return self.redis_connector.get(
            resource_name + ' - STATUS')

    def get_logged_rows_number(self, resource_name):
        data_range = self.redis_connector.get(
            resource_name + ' - ROWS')
        _, end = data_range.split('-')
        end = int(end)
        return end

    def log_start(self, resource_name):
        self.redis_connector.set(
            resource_name + ' - STATUS',
            'START')

    def log_completed(self, resource_name):
        self.redis_connector.set(
            resource_name + ' - STATUS',
            'COMPLETED')

    def log_progress(self, resource_name, data_range):
        start, end = data_range
        self.redis_connector.set(
            resource_name + ' - ROWS',
            f'{start}-{end}')

    def log_already_exists(self, resource_name):
        self.redis_connector.set(
            resource_name + ' - WARNING',
            'Ignored. Data already exists!')

    def clear_logs(self, resource_name):
        self.redis_connector.delete(resource_name + ' - STATUS')
        self.redis_connector.delete(resource_name + ' - ROWS')
        self.redis_connector.delete(resource_name + ' - WARNING')
