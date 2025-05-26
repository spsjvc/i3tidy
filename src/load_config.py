import json
import re
import os


def load_config(path=os.path.expanduser('~/.config/i3tidy/config.json')):
    try:
        config = {
            '__separator': ' | '
        }

        with open(path, 'r') as file:
            for class_name, config_data in json.load(file).items():
                config[class_name] = {
                    'class_alias': config_data.get('class_alias'),
                    'icon': config_data.get('icon'),
                    'name_regex': re.compile(config_data['name_regex']) if 'name_regex' in config_data else None,
                    'name_full': config_data.get('name_full', False)
                }

        return config
    except FileNotFoundError:
        return {}
