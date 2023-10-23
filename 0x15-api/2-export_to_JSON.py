#!/usr/bin/python3
"""Task 2"""

import json
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
    filename = f"{employee_id}.json"
    with open(filename, 'w', newline='') as file:
        json_list = []
        for task in todos:
            json_list.append({
                    "task": task.get('title'),
                    "completed": task.get('completed'),
                    "username": user.get('username')
                })
        json.dump({employee_id: json_list}, file)


if __name__ == "__main__":
    """ to check if the correct arguments are passed"""
    if len(sys.argv) == 2:
        display_todo_progress(int(sys.argv[1]))
