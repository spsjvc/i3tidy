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


def print_i3_info_separator():
    print("\n" + "=" * 100)


def print_i3_info(i3_connection):
    tree = i3_connection.get_tree()
    workspaces = tree.workspaces()

    if not workspaces:
        print("No workspaces found.")
        print_i3_info_separator()
        return

    for workspace in workspaces:
        print_i3_workspace_info(workspace)

    print_i3_info_separator()
