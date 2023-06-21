from datetime import date

import prompt
import scraper

from dotenv import load_dotenv
load_dotenv()

today = date.today().strftime("%Y%m%d")

scraper = scraper.BoletinScraper(date=today,id=288559)
result = scraper.scrape()

result['summary'] = prompt.summarize(result['content'])

print(result)
