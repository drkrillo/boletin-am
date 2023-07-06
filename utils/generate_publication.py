import json
import datetime

from utils import scraper, preprocessing, prompt

from dotenv import load_dotenv
load_dotenv()


def generate_publication(id):
    url = f'https://www.boletinoficial.gob.ar/detalleAviso/primera/{id}/20230704'
    type, content = scraper.scrape(url)
    print('Completed Scraping')
    chunks = preprocessing.chop(content)
    print('Completed Preprocessing')
    tags, score, summary = prompt.summarize(chunks)
    print('Completed Extraction')
    date = preprocessing.transform_date(content[-11:].replace('\n',''))
    publication = {
        'id': id,
        'date': date,
        'url': url,
        'type': type,
        'summary': summary,
        'tags': tags,
        'score': score
    }
    print('Publicated Created')
    print(publication)
    return publication
