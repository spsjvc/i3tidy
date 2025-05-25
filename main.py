#!/usr/bin/env python3

import i3ipc

def main():
    # Connect to i3
    i3 = i3ipc.Connection()

    print("Connected to i3!")
    print(f"Current workspaces: {i3.get_workspaces()}")

if __name__ == "__main__":
    main()
