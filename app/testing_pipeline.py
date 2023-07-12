import json
from utils.generate_publication import generate_publication

id = 289141
fn = '../data.json'

while True:
    publication = generate_publication(id)

    with open(fn, "r+") as file:
        data = json.load(file)
        data.append(publication)
        file.seek(0)
        json.dump(data, file)
    id += 1