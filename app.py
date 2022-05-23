# Extract all data from a list of 13 tables and loads it into Snowflake staging

import configparser
import time
import json
import threading
from threading import Thread

def get_config(config_section, list_name):
    # print('Retrieving configuration for object: ' + list_name)
    config_file = 'config.ini'
    # Get the current working directory
    try:
        app_config = open(config_file, 'r')
        app_config = app_config.read()
        app_config = configparser.ConfigParser()
        app_config.sections()
        app_config.read(config_file)
        result = app_config[config_section][list_name]
        return result
    except SystemExit:
        print('There is a fatal error with the configuration file, ' + str(config_file)
              + ' and entry: ' + config_section)

class Main:

    # Initialise Main
    def __init__(self, name):
        self.name = name

    # Main function
    print('Fetching app configuration from config.ini')
    max_parallel_operations = int(get_config('APP', 'MAX_PARALLEL_OPERATIONS'))
