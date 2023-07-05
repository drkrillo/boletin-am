from datetime import date
import time
import pandas as pd

from utils import scraper, preprocessing, prompt

from dotenv import load_dotenv
load_dotenv()


def generate_publication(id):
    url = f'https://www.boletinoficial.gob.ar/detalleAviso/primera/{id}/20230704'
    type, content = scraper.scrape(url)

    chunks = preprocessing.chop(content)
    tags, score, summary = prompt.summarize(chunks)
    date = content[-11:].replace('\n','')

    publication = {
        id: id,
        date: date,
        url: url,
        type: type,
        summary: summary,
        tags: tags,
        score: score
    }

    return publication
