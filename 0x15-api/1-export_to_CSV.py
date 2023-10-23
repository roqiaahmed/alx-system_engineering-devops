#!/usr/bin/python3
"""returns information about his/her TODO list progress.
"""

from requests import get
from sys import argv
import csv


if __name__ == "__main__":
    res = get("https://jsonplaceholder.typicode.com/users")
    data = res.json()

    for n in data:
        if n.get("id") == int(argv[1]):
            employee = n.get("name")

        res = get("https://jsonplaceholder.typicode.com/todos")
    data1 = res.json()

    file = "{}.csv".format(argv[1])
    row = []
    with open(file, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for i in data1:
            row = []
            if i.get("userId") == int(argv[1]):
                row.append(i['userId'])
                row.append(employee)
                row.append(i["completed"])
                row.append(i['title'])
                writer.writerow(row)
