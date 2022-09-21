import json
from time import sleep
import requests
from APICall import api_call
from Modes import get_mode
from savetojson import savedata

def generaterates(datadictionary : dict = get_mode()):
  input_dict = datadictionary['rates']

  for (key,val) in list(input_dict.items()):
    if int(float(val)) > 9.9:
      input_dict.pop(key)

  return input_dict