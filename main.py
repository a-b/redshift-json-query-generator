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
def parse_json(j):
    res = {}

    def parse(node, path = ''):
        if type(node) is dict:
            for key in node:
                parse(node[key], path + key + "_")
        elif type(node) is list:
            i = 0
            for element in node:
                parse(element, path + str(i) + "_")
                i += 1
        else:
            print(f"DEBUG: #{res}")
            res[path[:-1]]=node
    
    parse(j)
    return(res)

print(parse_json(json.loads(input_json())))