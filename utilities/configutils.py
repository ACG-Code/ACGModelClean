from configparser import ConfigParser
from base_settings import APPLICATION_PATH
import os

CONFIG_FILE = os.path.join(APPLICATION_PATH, 'config.ini')


def get_config(instance: str) -> dict:
    config = ConfigParser()
    config.read(CONFIG_FILE)
    _cloud = str_to_bool(config[instance]['cloud'])
    if _cloud:
        _config = {
            'base_url': config[instance]['address'],
            'namespace': 'LDAP',
            'verify': True,
            'async_requests_mode': True
        }
    else:
        _config = {
            'address': config[instance]['address'],
            'port': config[instance]['port'],
            'ssl': config[instance]['ssl'],
            'namespace': config[instance]['namespace'],
            'gateway': config[instance]['gateway']
        }
    return _config


def save_config(instance: str, config: dict) -> None:
    conf = ConfigParser()
    conf.read(CONFIG_FILE)
    conf[instance] = config
    conf.write(open(CONFIG_FILE, 'w'))


def retrieve_sections() -> list:
    _sections = ['']
    config = ConfigParser()
    config.read(CONFIG_FILE)
    for section in config.sections():
        _sections.append(section)
    return _sections


def retrieve_section_for_update(instance: str) -> dict:
    config = ConfigParser()
    config.read(CONFIG_FILE)
    return dict(config.items(instance))


def str_to_bool(string: str) -> bool:
    return string.lower() in ['y', 'yes', 't', 'true', 'on', '1']
