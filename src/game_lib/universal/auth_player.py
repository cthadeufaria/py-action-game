"""Class that stores information about an authenticated user."""
from typing import Tuple, TypedDict
import firebase  # type: ignore

ranking_type = TypedDict(
    "ranking_type", {"name": str, "points": int, "position": Tuple[int, int]}
)


class AuthPlayer:
    """Class that stores information about an authenticated user."""

    def __init__(self, name: str) -> None:
        """Initialize AuthPlayer instance."""
        self.user_id = None
        self.last_room = "main"
        self.name = name
        self.num_points = 0
        self.ranking: dict[str, ranking_type] = {
            "id": {"name": "Hero", "points": 0, "position": (800, 500)}
        }

        # Initialize firestore client
        fb_client = firebase.Firebase(
            {
                "apiKey": "AIzaSyC6fkyak3a9F4ozgj0XS7TQuQg3wxapbK8",
                "authDomain": "feupscape.firebaseapp.com",
                "databaseURL": "https://feupscape-default-rtdb.europe-west1.firebasedatabase.app",
                "projectId": "feupscape",
                "storageBucket": "feupscape.appspot.com",
            }
        )

        self.auth = fb_client.auth()
        self.db = fb_client.database()
        self.refresh_token = None

    def create_user(self, email: str, password: str) -> None:
        """Create firebase Auth user with email and password."""
        self.auth.create_user_with_email_and_password(email, password)
        self.db.child("ranking").child(self.user_id).set(
            {"points": 0, "position": (800, 500), "name": self.name}
        )
        self.login(email, password)

    def login(self, email: str, password: str) -> None:
        """Authenticate on firebase Auth with email and password."""
        user = self.auth.sign_in_with_email_and_password(email, password)
        self.user_id = user["localId"]
        self.refresh_token = user["refreshToken"]
        self.query_ranking()

    def renew_token(self) -> None:
        """Renew token to keep user authenticated before its 1-hour expiration."""
        user = self.auth.refresh(self.refresh_token)
        self.refresh_token = user["refreshToken"]

    def query_ranking(self) -> None:
        """Create snapshot listener to Firestore ranking doc."""
        if not bool(self.user_id):
            raise Exception("User is not authenticated")

        res = self.db.child("ranking").get()
        self.ranking = dict(res.val())

    def update_player_data(self, points: int, pos: Tuple[int, int]) -> None:
        """Update player's points in Firestore ranking doc."""
        if not bool(self.user_id):
            raise Exception("User is not authenticated")

        self.db.child("ranking").child(self.user_id).update(
            {"name": self.name, "points": points, "position": pos}
        )
