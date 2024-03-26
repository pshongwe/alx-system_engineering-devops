#!/usr/bin/python3
"""Exports data in CSV format."""
import csv
import requests
import sys


def export_to_csv(employee_id):
    """Exports the TODO list progress of an employee to a CSV file."""
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
    file_name = f'{employee_id}.csv'

    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([employee_id, username,
                            todo.get('completed'), todo.get('title')])


if __name__ == '__main__':
    export_to_csv(sys.argv[1])
