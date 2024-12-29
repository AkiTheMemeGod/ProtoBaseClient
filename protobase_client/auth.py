# protobase_client/auth.py

import requests

BASE_URL = "https://protobase.pythonanywhere.com/"


class ProtoBaseClient:
    def __init__(self):
        self.base_url = BASE_URL

    def signup_email(self, username, password, email):
        """Sign up with email."""
        url = f"{self.base_url}auth_api/email-signup/"
        params = {"usr": username, "pwd": password, "email": email}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 400:
            return response.json()
        else:
            return {"message": "Error signing up."}

    def signup_username(self, username, password):
        """Sign up with username."""
        url = f"{self.base_url}auth_api/user-signup/"
        params = {"usr": username, "pwd": password}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 400:
            return response.json()
        else:
            return {"message": "Error signing up."}

    def signin_email(self, username, password, email):
        """Sign in with email."""
        url = f"{self.base_url}auth_api/email-signin/"
        params = {"usr": username, "pwd": password, "email": email}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 400:
            return response.json()
        else:
            return {"message": "Error signing in."}

    def signin_username(self, username, password):
        """Sign in with username."""
        url = f"{self.base_url}auth_api/user-signin/"
        params = {"usr": username, "pwd": password}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 400:
            return response.json()
        else:
            return {"message": "Error signing in."}, response.status_code
