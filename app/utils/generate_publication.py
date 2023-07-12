import json
import datetime

from utils import scraper, preprocessing, prompt

from dotenv import load_dotenv
load_dotenv()


def generate_publication(url):
    type, content, date = scraper.scrape_article(url)
    print('Completed Scraping')

    chunks = preprocessing.chop(content)
    print('Completed Preprocessing')

    tags, score, summary = prompt.summarize(chunks)
    print('Completed Extraction')

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
