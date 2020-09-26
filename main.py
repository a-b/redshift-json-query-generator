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

def parse_json(j, path):
    # if j is None:
    #     print(j, type(j))
    #     return
    
    if isinstance(j, dict):
        for k,v in j.items():
            # print("-\t", k, type(v))
            parse_json(v, path + "." + k)

    if isinstance(j, list):
        for i in j:
            print("=", i)
            parse_json(i, "_")

    print(path)

parse_json(json.loads(input_json()), "")
