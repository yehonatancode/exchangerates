from src.APICall import api_call
from savetojson import usedata

Modes = {'DEV', 'PROD'}
MODE = 'DEV'
# MODE = 'PROD'
d = {}

def get_mode():
    if MODE == 'PROD':
        d = api_call()

#if we will add more modes, #todo elif
    else:
        d = usedata()

    return d

def set_mode(value : str):
    if value in Modes:
        MODE = value

