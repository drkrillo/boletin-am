import json
from utils.generate_publication import generate_publication
from utils.scraper import *

urls = today_urls()

print(urls)

for url in urls:
    type, content, date = scrape_article(url)
    print(type)
    print(content)
    print(date)
    print('***********')