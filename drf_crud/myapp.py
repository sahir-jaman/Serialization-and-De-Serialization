import requests
import json

URL = "http://127.0.0.1:8000/student-info/"

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)

    r = requests.get(url = URL, data = json_data)
    print(r.json())


def post_data():
    data = {
        'name': 'Boogs',
        'roll': 1234546,
        'city': 'Narail'
    }
    json_data = json.dumps(data)

    r = requests.post(url=URL, data = json_data)
    print(r.json())


def update_data():
    data = {
        'id': 6,
        'name': 'Muhammad',
        'roll': 134,
        'city': 'savar'
    }
    json_data = json.dumps(data)

    r = requests.put(url=URL, data = json_data)
    print(r.json())

def delete_data():
    data={'id':4}

    json_data = json.dumps(data)

    r = requests.delete(url=URL, data = json_data)
    print(r.json())

# Execute those 4 below funciton 1 by 1.
get_data()
# post_data()
# update_data()
# delete_data()