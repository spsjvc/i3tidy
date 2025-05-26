#!/usr/bin/env python3

import i3ipc

from src.get_workspace_name import get_workspace_name


def update_workspace_name(i3_connection, workspace):
    current_name = workspace.name
    target_name = get_workspace_name(workspace)

    if current_name != target_name:
        print(f'Renaming workspace {workspace.num}')
        print(f'    ├─ before: {current_name}')
        print(f'    └─ after:  {target_name}')
        print()

        try:
            i3_connection.command(f'rename workspace "{current_name}" to "{target_name}"')
        except i3ipc.CommandError as e:
            # This can happen if the old name is no longer valid (e.g., already renamed by another event)
            # or if the target name is identical after all (race condition with i3 state)
            print(f'Could not rename workspace "{current_name}" to "{target_name}": {e}. Refreshing state may resolve this.')
            # Attempt to rename using workspace number as a fallback for current name if it changed
            try:
                i3_connection.command(f'rename workspace number {workspace.num} to "{target_name}"')
            except i3ipc.CommandError as e2:
                print(f'Fallback rename for workspace number {workspace.num} to "{target_name}" also failed: {e2}')


def update(i3_connection):
    try:
        tree = i3_connection.get_tree()

        for workspace in tree.workspaces():
            update_workspace_name(i3_connection, workspace)
    except Exception as e:
        print(f'Error getting workspaces or updating names: {e}')


def on_window_event(i3_connection, event):
    update(i3_connection)


def main():
    i3_connection = i3ipc.Connection()

    update(i3_connection)

    i3_connection.on(i3ipc.Event.WINDOW_NEW, on_window_event)
    i3_connection.on(i3ipc.Event.WINDOW_CLOSE, on_window_event)
    i3_connection.on(i3ipc.Event.WINDOW_MOVE, on_window_event)
    i3_connection.on(i3ipc.Event.WINDOW_TITLE, on_window_event)

    i3_connection.main()


if __name__ == '__main__':
    main()
