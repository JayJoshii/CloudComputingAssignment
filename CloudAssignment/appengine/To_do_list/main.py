# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python38_app]
# [START gae_python3_app]
from flask import Flask


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route("/")
def display_list(tasks):
  if len(tasks) == 0:
    print("Your to-do list is empty.")
  else:
    print("Your to-do list:")
    for i, task in enumerate(tasks):
      print(f"{i+1}. {task}")

# function to add a new task
def add_task(tasks):
  new_task = input("Enter a new task: ")
  tasks.append(new_task)
  print(f"Task '{new_task}' added successfully.")

# function to mark a task as complete
def mark_complete(tasks):
  display_list(tasks)
  if len(tasks) == 0:
    return
  while True:
    try:
      task_number = int(input("Enter the number of the task to mark complete: ")) - 1
      if 0 <= task_number < len(tasks):
        del tasks[task_number]
        print("Task marked complete.")
        break
      else:
        print("Invalid task number. Please enter a valid number.")
    except ValueError:
      print("Invalid input. Please enter a number.")

def main():
  tasks = []
  while True:
    print("\nTo-Do List App")
    print("1. Display List")
    print("2. Add Task")
    print("3. Mark Task Complete")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
      display_list(tasks)
    elif choice == "2":
      add_task(tasks)
    elif choice == "3":
      mark_complete(tasks)
    elif choice == "4":
      print("Exiting...")
      break
    else:
      print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. You
    # can configure startup instructions by adding `entrypoint` to app.yaml.
    app.run(host="127.0.0.1", port=8080, debug=True)
# [END gae_python3_app]
# [END gae_python38_app]
