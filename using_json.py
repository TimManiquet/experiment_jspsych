import json

with open('results.js') as json_file:
    data = json.load(json_file)
    # data = json.load(json_file)

for i in range(len(data)):
    if 'task' in data[i].keys():
        print(data[i]['stimulus'])

data.keys()
len(data['response'])

data[1]['stimulus']