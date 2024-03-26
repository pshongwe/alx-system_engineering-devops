#!/usr/bin/python3
"""Exports data in JSON format for all employees."""
import json
import requests


def export_all_to_json():
    """Exports the TODO list data of all employees to a JSON file."""
    base_url = 'https://jsonplaceholder.typicode.com'
    users_url = f'{base_url}/users'
    todos_url = f'{base_url}/todos'

    try:
        users = requests.get(users_url).json()
        todos = requests.get(todos_url).json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return

    all_tasks = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        user_tasks = [
            {"username": username, "task": todo.get('title'),
             "completed": todo.get('completed')}
            for todo in todos if todo.get('userId') == user_id
        ]
        all_tasks[user_id] = user_tasks

    file_name = 'todo_all_employees.json'
    with open(file_name, 'w') as jsonfile:
        json.dump(all_tasks, jsonfile)


if __name__ == '__main__':
    export_all_to_json()
