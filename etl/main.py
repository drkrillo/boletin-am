import json
from utils.publication_pipeline import generate_publication
from utils.scraper import today_urls
from utils.loader import json_loader

urls = today_urls()
print(f"{len(urls)} Publications found.")
print('***************')

for i, url in enumerate(urls):
    print(f"Publication {i+1}")
    publication = generate_publication(url)
    json_loader(publication)
    print('***************')