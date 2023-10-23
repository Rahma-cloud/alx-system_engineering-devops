#!/usr/bin/python3
"""Task 0"""

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

    completed_tasks = [task for task in todos if task.get('completed')]
    total_tasks = len(todos)

    print(f"Employee {user.get('name')} is done with tasks\
            ({len(completed_tasks)}/{total_tasks}):")

    for task in completed_tasks:
        print(f"\t{task.get('title')}")


if __name__ == "__main__":
    """ to check if the correct arguments are passed"""
    if len(sys.argv) == 2:
        display_todo_progress(int(sys.argv[1]))
