import requests
from django.conf import settings
import json


def register(api_key, secret_key, **kwargs):
    endpoint = f'{settings.API_HOST}register/'
    first_name = kwargs.get('first_name')
    email = kwargs.get('email')
    last_name = kwargs.get('last_name')
    password = kwargs.get('password')
    payload = {
        "api_key": api_key,
        "secret_key": secret_key,
        "user": {
            "password": password,
            "email": email,
            "first_name": first_name,
            "last_name": last_name
        }

    }
    headers = {
        'Content-Type': 'application/json',

    }
    response = requests.request("POST", endpoint, headers=headers, data=json.dumps(payload))
    if response.status_code == 201:
        return "User Registered", True
    return json.loads(response.text)['error'], False


def login(username, password):
    endpoint = f'{settings.API_HOST}login/'

    payload = {

        "password": password,
        "username": username,

    }
    headers = {
        'Content-Type': 'application/json',

    }
    response = requests.request("POST", endpoint, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        return json.loads(response.text), True
    return "invalid credentials", False


def get_currency(token):
    endpoint = f'{settings.API_HOST}currency/'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Token {token}'

    }
    response = requests.request("GET", endpoint, headers=headers)

    if response.status_code == 200:
        return json.loads(response.text), True
    return "Error occured on server side", False
