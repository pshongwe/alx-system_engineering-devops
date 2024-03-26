#!/usr/bin/python3
"""Gathers data from an API and displays the TODO list
progress of a given employee."""
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [x.get("title") for x in todos if x.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(s)) for s in completed]
