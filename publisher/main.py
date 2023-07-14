from utils.reader import reader
from utils.preprocesser import sort_by
from utils.ranker import ranker


FILEPATH = '../data.json'


data = reader(FILEPATH)
print(data)
data = ranker(data, threshold=50)
print(data)
data = sort_by(data)

for pub in data:
    print(pub['score'])
    print(pub['summary'])
    print(pub['url'])
    print(pub['tags'])
    print("********************")