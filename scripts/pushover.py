import requests
from keys import *
from client import *

class pushover:
    
    def __init__(self, api_token, user_key):
        self.api_token = api_token
        self.user_key = user_key
        self.url = "https://api.pushover.net/1/messages.json"

    
    def send_message(self, message, title):
        data = {
            "token": self.api_token,
            "user": self.user_key,
            "message": message,
            "title": title
        }
        response = requests.post(self.url, data = data)
        if response.status_code == 200:
            print("Notification sent successfully!")
        else:
            print(f"Failed to send notification. Error: {response.status_code}")
            print(response.json())    