import json
import re


def load_config(path='config.json'):
    try:
        config = {}

        with open(path, 'r') as file:
            for class_name, config_data in json.load(file).items():
                config[class_name] = {
                    'icon': config_data['icon'],
                    'name_regex': re.compile(config_data['name_regex']) if 'name_regex' in config_data else None,
                    'name_full': config_data.get('name_full', False)
                }

        return config
    except FileNotFoundError:
        return {}
