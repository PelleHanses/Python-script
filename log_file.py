#!/usr/bin/python3
"""
log_file.php
Example of logging.

The function can be included in other scripts like this:
    from log_file import log_msg
    result = log_msg(level, msg)
"""

import datetime
import logging

# Set up the logging configuration
logging.basicConfig(
    filename="./log_file.log",                           # Specify the log file path
    level=logging.DEBUG,                                  # Set the logging level (INFO, DEBUG, WARNING, ERROR, etc.)
    format='%(asctime)s - %(levelname)s - %(message)s'   # Define the log message format
)

def log_msg(level, msg):
    """
    Logs a message with a specified level.

    Parameters:
    - level (str): The log level ('info', 'warning', 'error').
    - msg (str): The message to log.

    Returns:
    - bool: True if the log level is valid, False otherwise.
    """
    levels = {
        "debug": logging.debug,
        "info": logging.info,
        "warning": logging.warning,
        "error": logging.error
    }

    log_function = levels.get(level)
    if log_function:
        log_function(msg)
        return True
    else:
        logging.error(f"Invalid log level: {level}")
        return False

def example_function():
    try:
        # Perform some operations that may raise an exception
        result = 1 / 0  # This will raise a ZeroDivisionError
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        #or
        log_msg("error", f"An error occurred (2): {str(e)}")

def main():
    logging.info("Starting program")
    logging.warning("This is a warning message")

    example_function()

    logging.info("Program completed")


## Start
if __name__ == "__main__":
    main()
    result = log_msg("info", "Test of info")
    result = log_msg("warning", "Test of warning")
    result = log_msg("error", "Test of error")
    result = log_msg("debug", "Test of debug")
    result = log_msg("invalid", "Test of invalid level")
