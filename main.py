#!/usr/bin/env python3

import i3ipc
import time

def print_i3_window_info(window, window_index):
    print(f"  └─ App {window_index}:")
    print(f"    ├─ ID: {window.id}")
    print(f"    ├─ Name: '{window.name}'")
    print(f"    ├─ Class: '{window.window_class}'")
    print(f"    ├─ Instance: '{window.window_instance}'")
    print(f"    ├─ Role: '{window.window_role}'")


def print_i3_workspace_info(workspace):
    print(f"Workspace {workspace.num} (Name: '{workspace.name}')")
    windows = workspace.leaves()

    if not windows:
        print("  └─ (empty)")
        return

    for win_num, window in enumerate(windows, 1):
        print_i3_window_info(window, win_num)


def print_i3_info(i3_connection):
    tree = i3_connection.get_tree()
    workspaces = tree.workspaces()

    if not workspaces:
        print("No workspaces found.")
        print("=" * 100)
        return

    for workspace in workspaces:
        print_i3_workspace_info(workspace)

    print("\n" + "=" * 100)


def on_window_event(i3_conn, event):
    time.sleep(0.1)
    print_i3_info(i3_conn)


def main():
    i3_connection = i3ipc.Connection()

    print_i3_info(i3_connection)

    i3_connection.on(i3ipc.Event.WINDOW_NEW, on_window_event)
    i3_connection.on(i3ipc.Event.WINDOW_CLOSE, on_window_event)
    i3_connection.on(i3ipc.Event.WINDOW_MOVE, on_window_event)

    i3_connection.main()


if __name__ == "__main__":
    main()
