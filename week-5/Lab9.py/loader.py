import json
from pathlib import Path

input_file = Path(__file__).with_name("task.json")

with input_file.open("r", encoding="utf-8") as file:
    task = json.load(file)

print("Loaded JSON file:", input_file.name)

for task in task:
    status = "done" if task["is it done?"] else "not done"
    print(f'Task: {task["task"]}, Due: {task["due"]}, Status: {status}')