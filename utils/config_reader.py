import configparser
import os

def load_config():
    config = configparser.RawConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.properties')
    config.read(config_path)
    return config
