import json

import requests

from src.savetojson import savedata, save_mode

API_KEY = "e2KI8bQcyOFfFC8P2a5B5xF0Sz3fhBQk"
#For some reason direct access is denied, resulting in "insufficient key" although it is legal.
#Therefore, I used indirect access to the api, as used in specific_convert file.

# def generatecall():
#     api_url = "https://exchangeratesapi.io/documentation/"
#     command = f'https://api.exchangeratesapi.io/v1/latest? access_key = {API_KEY}'
#     print(command)
#     command2 = f'https://api.exchangeratesapi.io/v1/symbols'
#
#     payload = {}
#     headers= {
#       "apikey": API_KEY
#     }
#
#     response = requests.request("GET", command2, headers=headers, data = payload)
#
#     status_code = response.status_code
#     print(response.text)

def api_call():
    url = "https://api.apilayer.com/exchangerates_data/latest"

    payload = {}
    headers = {
        "apikey": API_KEY
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    input_dict = json.loads(response.text)
    to_save = save_mode()
    if to_save:
        savedata(input_dict)  # optional, incase we would like to change/add data to JSON mock file.
    return input_dict