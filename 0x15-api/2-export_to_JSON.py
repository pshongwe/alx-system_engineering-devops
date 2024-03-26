#!/usr/bin/python3
"""Exports data in JSON format."""
import json
import requests
import sys

def export_to_json(employee_id):
    """Exports the TODO list data of an employee to a JSON file."""
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    try:
        user = requests.get(user_url).json()
        todos = requests.get(todos_url).json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return

    username = user.get('username')
    tasks = [
        {"task": todo.get('title'), "completed": todo.get('completed'), "username": username}
        for todo in todos
    ]

    data = {employee_id: tasks}
    file_name = f'{employee_id}.json'

    with open(file_name, 'w') as jsonfile:
        json.dump(data, jsonfile)

if __name__ == '__main__':
    export_to_json(sys.argv[1])
