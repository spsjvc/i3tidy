#!/usr/bin/env python3

import i3ipc
import time

from debug import print_i3_info


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
