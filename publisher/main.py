from utils.reader import reader
from utils.preprocesser import sort_by
from utils.ranker import ranker


FILEPATH = '../data.json'


data = reader(FILEPATH)
data = ranker(data, threshold=30)
data = sort_by(data)

for pub in data:
    print(pub['score'])
    print(pub['summary'])
    print(pub['url'])
    print(pub['tags'])
    print("********************")