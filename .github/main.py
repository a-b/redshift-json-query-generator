import json

def input_json():
    return """
{
    "firstName": "Jane",
    "lastName": {"Doe": "Moe"},
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}
"""

data = json.loads(input_json())

for k,v in data.items():
    print(k, type(v), type(v) is list)
    


