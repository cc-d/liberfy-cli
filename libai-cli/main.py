#!/usr/bin/env python3
# main.py

import argparse
from typing import Optional
from parseargs import setup_argparse
from api import user, token as apitoken, authrequests, project, syncdir


def printinfo() -> None:
    token = apitoken.load_token()
    if token:
        print(f"Currently saved token: {token}")
    else:
        print("No token found.")


def main():
    parser = setup_argparse()
    args = parser.parse_args()

    if args.cmd.startswith('u'):
        act = args.act if args.act is not None else ''
        if act.startswith('c'):
            user.create(args.email, args.password)
        elif act.startswith('l'):
            user.tokenlogin(args.email, args.password)
        elif act.startswith('m'):
            user.me()
    # For now, since other functionality is not yet implemented, I've left out handling for the other commands.
    # You would expand upon these conditions as needed to integrate other actions related to Project, SyncDir, DirFile, etc.
    elif args.cmd == "info":
        printinfo()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
