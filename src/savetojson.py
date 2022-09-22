import json

mock_data = "mockdata.json"
new_data = "data.json"
# data = mock_data
data = new_data
def savedata(dictionary):

    # Serializing json
    json_object = json.dumps(dictionary, indent=4)

    # Writing to sample.json
    with open(data, "w") as outfile:
        outfile.write(json_object)

def usedata():
    with open('mockdata.json') as json_file:
        data = json.load(json_file)
        return data

def save_mode():
    if data == new_data:
        return True