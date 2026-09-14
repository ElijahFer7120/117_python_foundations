from pathlib import Path

input_file = Path(__file__).with_name("engines.txt")

with input_file.open("r", encoding="utf-8") as file:
    contents = file.read()
    
print("loaded file: ", input_file.name)
print(contents)

## this script reads the txt files containing the list of engines in my collection and displays it in the terminal. 