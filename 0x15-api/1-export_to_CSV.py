#!/usr/bin/python3
"""returns information about his/her TODO list progress.
"""

from requests import get
from sys import argv
import csv


if __name__ == "__main__":
    res1 = get("https://jsonplaceholder.typicode.com/users")
    data1 = res1.json()

    for n in data1:
        if n['id'] == int(argv[1]):
            employee = n['username']

    res2 = get("https://jsonplaceholder.typicode.com/todos")
    data2 = res2.json()
    row = []

    with open(argv[1] + '.csv', 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for i in data2:
            row = []
            if i['userId'] == int(argv[1]):
                row.append(i['userId'])
                row.append(employee)
                row.append(i["completed"])
                row.append(i['title'])
                writer.writerow(row)
