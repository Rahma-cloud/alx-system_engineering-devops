#!/usr/bin/python3
"""Task 1"""

import csv
import requests
import sys


def display_todo_progress(employee_id):
    """ display progress of employee"""
    user = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{employee_id}'
            ).json()
    todos = requests.get(
            f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
            ).json()
    filename = f"{employee_id}.csv"
    with open(filename, 'w', newline='') as file:
        csv_writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            csv_writer.writerow((
                    task.get('userId'), user.get('username'),
                    task.get('completed'),
                    task.get('title')
                ))


if __name__ == "__main__":
    """ to check if the correct arguments are passed"""
    if len(sys.argv) == 2:
        display_todo_progress(int(sys.argv[1]))
