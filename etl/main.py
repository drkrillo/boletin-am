import json
import time

import openai

from utils.publication_pipeline import generate_publication
from utils.scraper import today_urls
from utils.loader import json_loader

urls = today_urls()
print(f"{len(urls)} Publications found.")
print('***************')

for i, url in enumerate(urls):
    print(f"Publication {i+1}")

    while True:
        try:
            publication = generate_publication(url)
            break
        except openai.error.RateLimitError as error:
            print(error)
            time.sleep(20)

    json_loader(publication)
    print('***************')