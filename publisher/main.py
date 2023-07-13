from utils.reader import reader
from utils.preprocesser import sort_by
from utils.ranker import ranker

data = reader()
data = ranker(data)
data = sort_by(data)

for pub in data:
    print(pub['score'])
    print(pub['summary'])
    print(pub['tags'])
    print("********************")