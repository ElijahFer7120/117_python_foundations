from pathlib import Path

output_file = Path(__file__).with_name("engines.txt")

message_lines = [
    "Diecast Engines i owned in my collection",
    "--------------",
    "1. thomas",
    "2. henry",
    "3. gordon",
    "4. james",
    "5. oliver",
    "6. percy",
]

with output_file.open("w", encoding="utf-8") as file:
    for line in message_lines:
        file.write(line + "\n")
        
print("wrote file: ", output_file.name)
## this script writes the list of engines i owned in my collection to a text file. 