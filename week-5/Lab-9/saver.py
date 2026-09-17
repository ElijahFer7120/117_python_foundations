import json
from pathlib import Path


task = [
    {
        "task": "finish homework", 
        "due": "tomorrow",
        "is it done?": True
    }
,
    {
        "task": "watch kamen rider zeztz", 
        "due": "until it's finished",
        "is it done?": False
    }
,
    {
        "task": "watch the new thomas show",
        "due": "September 17",
        "is it done?": True
    }

]

output_file = Path(__file__).with_name("task.json")

with output_file.open("w", encoding="utf-8") as file:
    json.dump(task, file, indent=2)
    
print("Saved JSON file:", output_file.name)

