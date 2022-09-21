import json
def savedata(dictionary):

    # Serializing json
    json_object = json.dumps(dictionary, indent=4)

    # Writing to sample.json
    with open("mockdata.json", "w") as outfile:
        outfile.write(json_object)

def usedata():
    with open('mockdata.json') as json_file:
        data = json.load(json_file)
        print(data)