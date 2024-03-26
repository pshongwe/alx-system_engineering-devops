#!/usr/bin/python3
"""Gathers data from an API and displays the TODO list
progress of a given employee."""
import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]
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
    a = user.get('name')
    b = len(completed_tasks)
    c = len(todos)
    print(f"Employee {a} is done with tasks({b}/{c}): ")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")
