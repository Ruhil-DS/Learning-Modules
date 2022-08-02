# Day3
# 1st --> pip install pydantic
from pprint import pprint
from typing import List, Dict, Any, Optional

from pydantic import BaseModel, Json

import json

'''
pydantic is primarily a parsing library, not a validation library. 
Validation is a means to an end: building a model which conforms to the types and constraints provided.

In other words, pydantic guarantees the types and constraints of the output model, not the input data.
'''


class test(BaseModel):
    id: int
    name = "Pushpak"
    subjects: List[int]


# https://pydantic-docs.helpmanual.io/usage/models/#model-properties
# ^ for more methods available with the class that we defined. eg - .schema()
# print(test(id="10", subjects=['1', '2', '15']).dict())


# ---------------

class num_values(BaseModel):
    x: int
    y: float


class test(BaseModel):
    id: int
    name = "Pushpak"
    subjects: List[num_values]


# Loss of info, above doc explained.


test_var = test(id=15.23, subjects=[{'x': 100, 'y': '255'}]).dict()

# print(test_var)

# Also check ->
# https://pydantic-docs.helpmanual.io/usage/models/#error-handling

# --------
# Testing with an API -->
# Running my API in another terminal on localhost:5000
import requests
import json

base_url = "http://localhost:5000/api"
resp = requests.post(f"{base_url}/login/",
                     json={'username': 'pushpak', 'password': 'abcd'},
                     headers={'Content-Type': 'application/json'})

# JWT token
token = resp.json()['access_token']

resp = requests.get(f"{base_url}/dashboard/",
                    headers={
                        'Content-Type': 'application/json',
                        'Authorization': f'Bearer {token}'
                    })

data = resp.json()
# print(data)
# pprint(data)
'''
{
    'streak': '1', 
    'tracker_count': '3', 
    'member_since': '172 days', 
    'trackers': {28: ['Numbersss', 'num', '2022-07-06T19:16:44.994'], 
                 38: ['lets see', 'time_dur', '2022-03-06T23:17'], 
                52: ['lets see', 'bool', '2022-03-07T14:30']}, 
    'graph_path': 'static/images/homepage_pushpak.png'
}
'''

data_temp = {
    'streak': '1',
    'tracker_count': '3',
    'member_since': '172 days',
    'trackers': {'id': ['Numbersss', 'num', '2022-07-06T19:16:44.994', 12]},
    'graph_path': 'static/images/homepage_pushpak.png'
}

# streak -> int
# tracker_count -> int
# member_since -> str
# trackers -> dict -> key: int, value: list
# graph_path -> str


class Trackers(BaseModel):
    id: List[str]


class DashboardJSON(BaseModel):
    streak: int
    tracker_count: int
    member_since: str
    trackers: Trackers = None
    graph_path: str


# print("========")
# print([(x, data[x]) for x in data])
# print("========")

test_var = DashboardJSON(**data_temp)

print("========")
print(test_var)
print("========")