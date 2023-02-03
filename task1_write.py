import json

data = {}

data['people'] = []
data['people'].append({
    'fname': 'Vadim',
    'lname': 'Liubin',
    'status': 'admin'
})
data['people'].append({
    'fname': 'Nick',
    'lname': 'Bush',
    'status': 'user'
})
data['people'].append({
    'fname': 'Helen',
    'lname': 'Jonse',
    'status': 'user'
})

with open('data.txt', "w") as outfile:
    json.dump(data, outfile)