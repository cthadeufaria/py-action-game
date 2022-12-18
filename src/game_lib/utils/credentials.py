"""Auxiliary functions to get and set data to/from credentials file."""
import json
import os.path
from .engine import get_absolute_path

# SORRY BOSS, STORING LOCALLY IS PRETTY UNSAFE, BUT I HAVE A DEADLINE


def get_credentials() -> dict[str, str] | None:
    """Retrieve credential dict from credentials file."""
    credentials = None
    credentials_path = get_absolute_path(__file__, "..", "..", "secret.json")
    if os.path.isfile(credentials_path):
        with open(credentials_path, "r", encoding="utf-8") as credentials_file:
            credentials = json.load(credentials_file)
    return credentials


def set_credentials(name: str, email: str, password: str) -> None:
    """Write file with provided email and password."""
    credentials_path = get_absolute_path(__file__, "..", "..", "secret.json")
    with open(credentials_path, "w", encoding="utf-8") as credentials_file:
        json.dump(
            {
                "name": name.lower().strip(),
                "email": email.lower().strip(),
                "password": password.lower().strip(),
            },
            credentials_file,
        )
