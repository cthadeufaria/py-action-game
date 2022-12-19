"""Auxiliary functions to get and set data to/from credentials file."""
import json
import os
import sys

# Get path of current running application, both for executable and interactive mode
if getattr(sys, "frozen", False):
    application_path = os.path.dirname(os.path.realpath(sys.executable))
else:
    application_path = os.path.dirname(__file__)

# SORRY BOSS, STORING LOCALLY IS PRETTY UNSAFE, BUT I HAVE A DEADLINE
credentials_path = os.path.join(application_path, "secret.json")


def get_credentials() -> dict[str, str] | None:
    """Retrieve credential dict from credentials file."""
    credentials = None
    if os.path.isfile(credentials_path):
        with open(credentials_path, "r", encoding="utf-8") as credentials_file:
            credentials = json.load(credentials_file)
    return credentials


def set_credentials(name: str, email: str, password: str) -> None:
    """Write file with provided email and password."""
    with open(credentials_path, "w", encoding="utf-8") as credentials_file:
        json.dump(
            {
                "name": name.lower().strip(),
                "email": email.lower().strip(),
                "password": password.lower().strip(),
            },
            credentials_file,
        )
