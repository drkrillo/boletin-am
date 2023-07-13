import json

def reader():
    f = open('../data.json')
    data = json.load(f)
    
    return data