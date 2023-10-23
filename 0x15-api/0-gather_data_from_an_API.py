#!/usr/bin/python3
"""Task 0"""

import requests


def display_todo_progress(employee_id):
    user = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{employee_id}'
            ).json()
    todos = requests.get(
            f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
            ).json()

    completed_tasks = [task for task in todos if task['completed']]
    total_tasks = len(todos)

    print(f"Employee {user['name']} is done with tasks\
            ({len(completed_tasks)}/{total_tasks}):")

    for task in completed_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    employee_id = 2
display_todo_progress(employee_id)
