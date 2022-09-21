import requests

#For some reason direct access is denied, resulting in "insufficient key" although it is legal.
#Therefore, I used indirect access to the api, as used in specific_convert file.
def generatecall():
    API_KEY = "e2KI8bQcyOFfFC8P2a5B5xF0Sz3fhBQk"
    api_url = "https://exchangeratesapi.io/documentation/"
    command = f'https://api.exchangeratesapi.io/v1/latest? access_key = {API_KEY}'
    print(command)
    command2 = f'https://api.exchangeratesapi.io/v1/symbols'

    payload = {}
    headers= {
      "apikey": "e2KI8bQcyOFfFC8P2a5B5xF0Sz3fhBQk"
    }

    response = requests.request("GET", command2, headers=headers, data = payload)

    status_code = response.status_code
    print(response.text)

