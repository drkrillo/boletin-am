from datetime import date
from csv import writer
import time
import pandas as pd

import boletin
import scraper
import preprocessing
import prompt

from dotenv import load_dotenv
load_dotenv()

id = max(pd.read_csv('data.csv', delimiter='|').id)
on = True

while on:
    article = boletin.BoletinObject(
        date=date.today(),
        id=id,
    )
    try:
        article.type, article.content = scraper.scrape(article.url)

        chunks = preprocessing.chop(article.content)
        summary = prompt.summarize(chunks)
        article.date = summary['date']
        article.summary = summary['summary']

        row = [
            article.content[-11:].replace('\n',''),
            article.id,
            article.url,
            article.type,
            article.summary,
        ]
        with open('data.csv', 'a', newline='') as f_object:
            writer_object = writer(f_object, delimiter='|')
            writer_object.writerow(row)
            f_object.close()

        print(f'Done! {id}')
        time.sleep(15)

    except AttributeError as error:
        on = False
    finally:
        id += 1