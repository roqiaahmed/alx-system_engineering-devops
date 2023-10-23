#!/usr/bin/python3
"""returns information about his/her TODO list progress.
"""

from requests import get
from sys import argv
import json


if __name__ == "__main__":
    row = []
    new_dict = {}
    f_dict = {}
    res_1 = get("https://jsonplaceholder.typicode.com/users").json()
    res_2 = get("https://jsonplaceholder.typicode.com/todos").json()

    for n in res_1:
        if n['id'] == int(argv[1]):
            username = n['username']
            user_id = n['id']

    for i in res_2:
        if i['userId'] == int(argv[1]):
            new_dict["task"] = i['title']
            new_dict["completed"] = i['completed']
            new_dict["username"] = username
            row.append(new_dict)

    f_dict[user_id] = row
    json_dict = json.dumps(f_dict)
    with open(argv[1] + '.json', 'w') as file:
        file.write(json_dict)
