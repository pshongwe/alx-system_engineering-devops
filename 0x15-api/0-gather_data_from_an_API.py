#!/usr/bin/python3
"""Gathers data from an API and displays the TODO list
progress of a given employee."""
import requests
import sys


def get_todo_list_progress(employee_id):
    """Fetches and displays the TODO list progress
    of an employee with the given ID."""
    # Base URL for the API
    api_url = 'https://jsonplaceholder.typicode.com'

    # Fetch the user data
    user_url = f'{api_url}/users/{employee_id}'
    user_response = requests.get(user_url)
    user_data = user_response.json()

    # Fetch the user's TODOs
    todos_url = f'{api_url}/todos?userId={employee_id}'
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate progress
    total_tasks = len(todos_data)
    completed_tasks = len([todo for todo in todos_data if todo['completed']])
    employee_name = user_data['name']

    # Display progress
    en = employee_name
    ag = f'{completed_tasks}/{total_tasks}'
    print(f'Employee {en} is done with tasks({ag}):')
    for todo in todos_data:
        if todo['completed']:
            print(f'\t {todo["title"]}')


if __name__ == '__main__':
    get_todo_list_progress(int(sys.argv[1]))
