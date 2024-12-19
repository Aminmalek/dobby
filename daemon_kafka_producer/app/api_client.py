import requests

class APIClient:
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_data(self):
        response = requests.get(self.api_url)
        response.raise_for_status()
        return response.json()["data"]
