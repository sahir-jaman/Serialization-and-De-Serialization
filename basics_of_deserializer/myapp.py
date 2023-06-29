import requests
import json

URL = "http://127.0.0.1:8000/student-create/"

data = {
    'name': 'pritam puri',
    'roll': 103,
    'city': "Delhi",
}

json_data = json.dumps(data)

r = requests.post(url = URL, data = json_data)
print(r)

data = r.json()
print(data)