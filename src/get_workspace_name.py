from .load_config import load_config


def get_workspace_name(workspace, config=load_config()):
    leaves = workspace.leaves()

    if not leaves:
        return str(workspace.num)

    apps = []

    for leaf in leaves:
        window_class = leaf.window_class
        window_name = leaf.name

        app_representation = ''
        app_config_entry = config.get(window_class)

        if app_config_entry:
            icon = app_config_entry['icon']
            final_name_part = ''

            if app_config_entry.get('name_full', False) and window_name:
                final_name_part = window_name
            elif app_config_entry.get('name_regex') and window_name:
                match = app_config_entry['name_regex'].search(window_name)

                if match:
                    final_name_part = match.group(1) if len(match.groups()) > 0 else match.group(0)
            elif icon is None:
                window_class_alias = app_config_entry.get('class_alias')
                final_name_part = window_class_alias if window_class_alias else window_class

            if final_name_part:
                icon_with_padding = f'{icon} ' if icon else ''
                app_representation = f'{icon_with_padding}{final_name_part}'
            else:
                app_representation = icon
        else:
            app_representation = f'{window_class}'

        if app_representation:
            apps.append(app_representation)

    if not apps:
        return str(workspace.num)

    return f'{workspace.num}: {config.get('__separator').join(apps)}'
