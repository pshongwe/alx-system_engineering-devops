#!/usr/bin/python3
"""Gathers data from an API and displays the TODO list
progress of a given employee."""
import requests
import sys


def get_todo_list_progress(employee_id):
    """Fetches and displays the TODO list progress
    of an employee with the given ID."""
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos"

    try:
        user = requests.get(user_url).json()
        todos = requests.get(todos_url, params={"userId": employee_id}).json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return

    completed_tasks = [todo for todo in todos if todo.get("completed")]
    print(f"Employee {user.get('name')} is done with tasks({len(completed_tasks)}/{len(todos)}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")

if __name__ == '__main__':
    get_todo_list_progress(int(sys.argv[1]))
