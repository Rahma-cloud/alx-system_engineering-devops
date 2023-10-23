#!/usr/bin/python3
"""Task 1"""

import requests
import sys
import csv


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
        print("\t", task.get('title'))
    export_to_csv(employee_id, user.get('username'), completed_tasks)


def export_to_csv(user_id, username, tasks):
    """export to csv file"""
    filename = f"{user_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
                ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
                )
    for task in tasks:
        writer.writerow(
                [user_id, username, str(
                    task.get('completed')), task.get('title')]
                )


if __name__ == "__main__":
    """ to check if the correct arguments are passed"""
    if len(sys.argv) == 2:
        export_to_csv(user_id, username, tasks)
