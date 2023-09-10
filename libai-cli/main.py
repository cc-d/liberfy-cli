# main.py

import argparse
from api import login_user, register_user
from utils import save_token, load_token


def login(args) -> None:
    response = login_user(args.email, args.password)
    if response.status_code == 200:
        token = response.json()
        token = token['access_token']
        print(token)
        save_token(token)
        print(f"Logged in successfully. Token saved.")
    else:
        print(f"Login failed with error: {response.text}")


def register(args) -> None:
    response = register_user(args.email, args.password)
    if response.status_code == 200:
        print("Successfully registered.")
    else:
        print(f"Registration failed with error: {response.text}")


def display_info(args) -> None:
    token = load_token()
    if token:
        print(f"Currently saved token: {token}")
    else:
        print("No token found.")


def setup_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Liberfy CLI")

    # Add a layer for the resource (e.g., user)
    resource_parsers = parser.add_subparsers(title="resource", dest="resource")
    user_parser = resource_parsers.add_parser(
        "user", help="User-related commands"
    )

    # Add commands for each resource
    user_commands = user_parser.add_subparsers(title="commands", dest="command")

    # Login
    login_parser = user_commands.add_parser(
        "login", help="Login to your account"
    )
    login_parser.add_argument("email", type=str, help="Your email address")
    login_parser.add_argument("password", type=str, help="Your password")

    # Register
    register_parser = user_commands.add_parser(
        "register", help="Register a new account"
    )
    register_parser.add_argument(
        "email", type=str, help="Your email address for registration"
    )
    register_parser.add_argument(
        "password", type=str, help="Your password for registration"
    )

    # Display Info (assuming info is a user command)
    info_parser = user_commands.add_parser("info", help="Display user info")

    return parser


def main():
    parser = setup_argparse()
    args = parser.parse_args()

    if args.resource == "user":
        if args.command == "login":
            login(args)
        elif args.command == "register":
            register(args)
        elif args.command == "info":
            display_info(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
