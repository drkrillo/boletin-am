from datetime import date
from csv import writer
import time

import boletin
import scraper
import preprocessing
import prompt

from dotenv import load_dotenv
load_dotenv()

id = 288549
on = True

while id <= 288648:
    article = boletin.BoletinObject(
        date=date.today(),
        id=id,
    )
    try:
        article.type, article.content = scraper.scrape(article.url)

        chunks = preprocessing.chop(article.content)
        social, economic, sustainable, politic, summary = prompt.summarize(chunks)
        article.date = article.content[-11:].replace('\n','')
        article.summary = summary

        row = [
            article.date,
            article.id,
            article.url,
            article.type,
            article.summary,
            social,
            economic,
            sustainable,
            politic,
        ]

        print("******************")
        print(social, economic, sustainable, politic)
        print(summary)
        
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