from config import RESOURCE_NAME, DATA_URL
from src.data_processor import Writer
from src.strategies import CosmosDBSavingStrategy, RedisLoggingStrategy, ConsoleLoggingStrategy, ConsoleOutputStrategy
import config


def main():
    print('\tLab 4')

    if config.STRATEGY == 'COSMOS':
        handler_strategy = CosmosDBSavingStrategy
        logger_strategy = RedisLoggingStrategy
    elif config.STRATEGY == 'CONSOLE':
        handler_strategy = ConsoleOutputStrategy
        logger_strategy = ConsoleLoggingStrategy

    dp = Writer(resource_name=RESOURCE_NAME, url_template=DATA_URL,
                       data_handler_strategy=handler_strategy,
                       logger_strategy=logger_strategy)
    dp.process_data()

    print('Done.')


if __name__ == '__main__':
    main()
