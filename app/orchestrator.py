import json
from utils.publication_pipeline import generate_publication
from utils.scraper import *

urls = today_urls()

print(urls)

for url in urls:
    publication = generate_publication(url)