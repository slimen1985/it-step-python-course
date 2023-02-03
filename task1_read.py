import json

with open('data.txt') as json_file:
    data = json.load(json_file)
    for p in data['people']:
        print('fname: ' + p['fname'])
        print('lname: ' + p['lname'])
        print('status: ' + p['status'])
        print('')