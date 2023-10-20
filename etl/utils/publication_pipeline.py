import json
import datetime
import openai
import time 

from utils import scraper, preprocesser, prompt

from dotenv import load_dotenv
load_dotenv()


def generate_publication(url):
    type, content = scraper.scrape_article(url)
    print('Completed Scraping')

    chunks = preprocesser.chop(content)
    date = datetime.date.today()
    print('Completed Preprocessing')

    try:
        tags, score, summary = prompt.summarize(chunks)
    except openai.error.APIConnectionError as error:
        print(error, "\n Retrying in 20s...")
        time.sleep(20)
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
