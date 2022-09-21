import json
from time import sleep

import requests

from savetojson import savedata

def generaterates():
  url = "https://api.apilayer.com/exchangerates_data/latest"

  payload = {}
  headers= {
    "apikey": "e2KI8bQcyOFfFC8P2a5B5xF0Sz3fhBQk"
  }

  response = requests.request("GET", url, headers=headers, data = payload)
  input_dict = json.loads(response.text)
  # output_dict = [x for x in input_dict if x['rates'] < 10]
  savedata(input_dict)
  d = list()
  ans = dict()
  d = input_dict['rates']
  # print(input_dict['rates'].values())
  for (key,val) in list(d.items()):
    if int(float(val)) > 9.9:
      d.pop(key)

  print(d)
  # # print(data)

  # for (key,value) in data:
  #   if(value < 10):
  #     del response.text[key]
  # # print(data)
  # status_code = response.status_code
  # print(response.text)
