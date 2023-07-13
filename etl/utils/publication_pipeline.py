import json
import datetime

from utils import scraper, preprocesser, prompt

from dotenv import load_dotenv
load_dotenv()


def generate_publication(url):
    type, content = scraper.scrape_article(url)
    print('Completed Scraping')

    chunks = preprocesser.chop(content)
    date = datetime.date.today()
    print('Completed Preprocessing')

    tags, score, summary = prompt.summarize(chunks)
    print('Completed Extraction')

    publication = {
        'date': str(date),
        'url': url,
        'type': type,
        'summary': summary,
        'tags': tags,
        'score': score
    }
    print('Publication Created')
    print(publication)

    return publication
