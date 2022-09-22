from src.Modes import get_mode


def generaterates(datadictionary : dict = get_mode()):
  input_dict = datadictionary['rates']

  for (key,val) in list(input_dict.items()):
    if int(float(val)) > 9.9:
      input_dict.pop(key)

  return input_dict