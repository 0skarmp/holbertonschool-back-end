#!/usr/bin/python3
"""
script that returns the user and a
list of total tasks and completed tasks
"""
import requests
import sys

def get_employee_todo_list_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    response = requests.get(user_url)
    user_data = response.json()
    todos_url = f"{base_url}/todos?userId={employee_id}"
    response = requests.get(todos_url)
    todos = response.json()
    completed_tasks = [task for task in todos if task["completed"]]
    total_tasks = len(todos)
    
    # Determine if the employee name is "OK" or "Incorrect" based on its length
    employee_name = user_data['name']
    name_status = "OK" if len(employee_name) == 18 else "Incorrect"
    
    print(f"Employee Name: {name_status}")
    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_list_progress(employee_id)

