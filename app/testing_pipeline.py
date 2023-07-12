import pandas as pd
from utils.generate_publication import generate_publication

df = pd.read_csv('../data.csv')

id = 289141

while True:
    publication = generate_publication(id)
    row = [
        publication['jd'],
        publication['date'],
        publication['url'],
        publication['type'],
        publication['summary'],
        publication['tags'],
        publication['score']
    ]

    df.loc[-1] = row
    
    df.to_csv(
        df,
        delimiter='|',
        econding='latin_1'
    )