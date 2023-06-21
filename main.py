from datetime import date
from datetime import timedelta

import boletin
import scraper
import preprocessing
import prompt

from dotenv import load_dotenv
load_dotenv()

article = boletin.BoletinObject(date=date.today() - timedelta(days = 30),id=288610)

article.content = scraper.scrape(article.url)
chunks = preprocessing.chop(article.content)
article.summary = prompt.summarize(chunks)

print(article.date)
print(article.summary)