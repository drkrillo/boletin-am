import json
from utils.generate_publication import generate_publication
from utils.scraper import *

urls = today_urls()

print(urls)

for url in urls:
    publication = generate_publication(url)