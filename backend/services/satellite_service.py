# services/satellite_service.py

import requests
import os
from dotenv import load_dotenv

load_dotenv()


class SatelliteService:

    def __init__(self):

        self.api_key = os.getenv(
            "NASA_API_KEY"
        )

    def fetch_satellite_data(self):

        url = (
            f"https://api.nasa.gov/planetary/apod"
            f"?api_key={self.api_key}"
        )

        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()

            return {

                "title": data.get("title"),

                "date": data.get("date"),

                "image_url": data.get("url"),

                "description":
                data.get("explanation")
            }

        return {

            "error":
            "Failed to Fetch Satellite Data"
        }