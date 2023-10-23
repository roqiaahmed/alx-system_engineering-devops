#!/usr/bin/python3
"""returns information about his/her TODO list progress.
"""

from requests import get
from sys import argv


if __name__ == "__main__":
    res = get("https://jsonplaceholder.typicode.com/users")
    data = res.json()
    all_tasks = 0
    completed = 0
    tasks = []

    for n in data:
        if n.get("id") == int(argv[1]):
            employee = n.get("name")

    res = get("https://jsonplaceholder.typicode.com/todos")
    data1 = res.json()

    for i in data1:
        if i.get("userId") == int(argv[1]):
            all_tasks += 1
            if i.get("completed") is True:
                completed += 1
                tasks.append(i.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(employee, completed,
                                                          all_tasks))
    for i in tasks:
        print("\t {}".format(i))
