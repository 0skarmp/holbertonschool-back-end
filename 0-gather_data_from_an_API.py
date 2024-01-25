#!/usr/bin/python3
"""
This script retrieves data from the JSONPlaceholder API,
list of total tasks and completed tasks
"""
import requests
import sys
url = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    """ fetches the TODO list user based on the user ID """
    response_todos = requests.get(f"{url}/todos?userId={sys.argv[1]}")
    response_users = requests.get(f"{url}/users/{sys.argv[1]}")

    todos = response_todos.json()
    user = response_users.json().get('name')

    done_taks = list()
    for todo in todos:
        """check if each task is completed (based on the 'completed' field).
        If it's completed, you add it to the done_tasks"""
        if todo.get('completed'):
            done_taks.append(todo)
    print(
        f"Employee {user} is done with tasks({len(done_taks)}/{len(todos)}):")
    for todo in done_taks:
        """the number of completed tasks, and the titles of completed tasks."""
        print(f"\t {todo.get('title')}")
