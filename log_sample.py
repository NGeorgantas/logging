
import logging.config
import json
import pathlib
import employee # noqa
import atexit
from mylogger import LogContext
import asyncio

# logger = logging.getLogger("my_app")


def setup_logging():
    config_file = pathlib.Path("logging_configs/config_2.json")
    with open(config_file) as f_in:
        config = json.load(f_in)
    logging.config.dictConfig(config)




# setup_logging()


def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    try:
        result = x / y
    except ZeroDivisionError as e:
        logger.error("Error occurred: %s", e)
        return None
    return result


async def main():
    print("something")
    setup_logging()

    num_1 = 10
    num_2 = 0

    add_result = add(num_1, num_2)
    logger.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

    sub_result = subtract(num_1, num_2)
    logger.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

    mul_result = multiply(num_1, num_2)
    logger.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

    div_result = divide(num_1, num_2)
    logger.warning('Div: {} / {} = {}'.format(num_1, num_2, div_result))

if __name__ == '__main__':
    logger = logging.getLogger("my_app")
    with LogContext():
        asyncio.run(main())  # Your main function


# num_1 = 10
# num_2 = 0

# add_result = add(num_1, num_2)
# logger.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

# sub_result = subtract(num_1, num_2)
# logger.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

# mul_result = multiply(num_1, num_2)
# logger.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

# div_result = divide(num_1, num_2)
# logger.warning('Div: {} / {} = {}'.format(num_1, num_2, div_result))
