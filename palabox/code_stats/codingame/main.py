"""CodinGame stats."""

import json
from dataclasses import asdict

import dacite
import requests

from .types import CodinGameStats


def get_user_stats(userid: str) -> CodinGameStats:
    """Get user stats."""
    response = requests.post(
        "https://www.codingame.com/services/CodinGamer/findCodingamePointsStatsByHandle",
        json=[userid],
    )
    if response.ok:
        return dacite.from_dict(CodinGameStats, response.json())
    else:
        raise ValueError(
            "Problem with the request %s, '%s'" % (response, response.content.decode())
        )


if __name__ == "__main__":
    data = get_user_stats("8c4c1d3cf92a07fd755428fbc86744fc2575773")
    with open("test.json", "w") as file:
        json.dump(asdict(data), file, indent=2)