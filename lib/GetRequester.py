import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # Sends an HTTP GET request and returns the response body as bytes
        response = requests.get(self.url)
        return response.content  # Return the raw response in bytes

    def load_json(self):
        # Uses get_response_body() and parses it as JSON
        response_body = self.get_response_body()
        return json.loads(response_body)  # Parse the byte response to JSON
