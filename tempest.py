"""
Tempest Weather Service and MongoDB Backend
"""
from pprint import pprint
from os import environ

from pymongo import MongoClient
import requests


def get_station_data(station_id: int, token: str) -> requests.Response:
    """Get Station Data

    :param station_id: The Station ID for the TempestWx API.
    :param token: The API Token used for the TempestWx API.

    :rtype: `requests.Response`
    """
    tempest_url: str = (
        f"https://swd.weatherflow.com/swd/rest/observations/station/{station_id}"
    )
    tempest_url_params: dict[str, str] = {"token": token}
    response = requests.get(url=tempest_url, params=tempest_url_params, timeout=10)
    return response


def add_obs(observation: requests.Response) -> None:
    """
    Adds an `observation` to the DB.

    :param observation: The `Response` from the TempestWx API.
    """
    pprint(observation.json())
    with MongoClient(host="localhost", port=8081) as client:
        db = client.get_database("tempest")
        db.SanMarco.insert_one(observation.json())


if __name__ == "__main__":
    token = environ.get("TEMPEST_TOKEN", "")
    san_marco: int = 117515
    data = get_station_data(san_marco, token)
    add_obs(data)

    # with MongoClient(host="localhost", port=8081) as client:
    #     db = client.get_database("tempest")
    #     pprint(db.SanMarco.find_one())
