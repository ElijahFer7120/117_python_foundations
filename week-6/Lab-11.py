import json
from pathlib import Path

input_file = Path(__file__).with_name("sonic.json")

with input_file.open("r", encoding="utf-8") as file:
    response_data = json.load(file)
    

print("Name:", response_data["name"])
print("Power:", response_data["stats"]["power"])
print("Speed:", response_data["stats"]["speed"])
print("Location:", response_data["location"][0]["zone"])
print("Status:", response_data["location"][0]["status"])