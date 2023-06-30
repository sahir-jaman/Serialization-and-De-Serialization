import requests
import json

URL = "http://127.0.0.1:8000/student-info/"

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id': id}

    json_data = json.dumps(data)
    headers = {'content-Type' : 'application/json'}


    r = requests.get(url = URL, headers = headers, data = json_data)
    print(r.json())


def post_data():
    data = {
        'name': 'Boogs',
        'roll': 1234546,
        'city': 'Narail'
    }
    headers = {'content-Type' : 'application/json'}
    json_data = json.dumps(data)

    r = requests.post(url=URL,headers = headers, data = json_data)
    print(r.json())

def update_data():
    data = {
        'id': 3,
        'name': 'Md. Refayet',
        'roll': 7,
        'city': 'Dhaka'
    }
    json_data = json.dumps(data)
    headers = {'content-Type' : 'application/json'}

    r = requests.put(url=URL,headers=headers, data = json_data)
    print(r.json())

def delete_data():
    data={'id':4}

    json_data = json.dumps(data)
    headers = {'content-Type' : 'application/json'}

    r = requests.delete(url=URL,headers=headers, data = json_data)
    print(r.json())

# Execute those 4 below funciton 1 by 1.
# get_data(1)
# post_data()
update_data()
# delete_data()