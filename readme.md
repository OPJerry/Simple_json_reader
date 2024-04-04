json_reader.py

1. pip install pydantic
2. pip install rich
3. pip install json

in line 32 of json_reader.py - in the main() method, we need to provide the path to the json file instead of r'XXX'

for example:
r'C:\Users\Admin\Desktop\example.json'

when you run json_reader.py
code will return False if resource = "*"
 else it will return True

I am confident that this code possesses significant potential for expansion, welcoming the addition of new variables or modifications.