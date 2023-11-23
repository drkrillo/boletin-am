import json
import time
import datetime

import openai

from utils import scraper, loader, prompt, preprocesser


areas_of_interest = ["Resoluciones", "Leyes", "Decretos", "Disposiciones"]
def main():
    urls, _ = scraper.today_urls()
    print(f"{len(urls)} Publications found.")
    print('***************')

    for i, url in enumerate(urls):
        print(f"Publication {i+1} of {len(urls)+1}")
        type, area, content, _ = scraper.scrape_article(url)
        print('Completed Scraping')

        if type  in areas_of_interest:
            chunks = preprocesser.chop(content)
            date = datetime.date.today()
            print('Completed Preprocessing')

            try:
                tags, score, summary = prompt.summarize(chunks)
            except (
                openai.error.APIConnectionError, 
                openai.error.APIError,
                openai.error.ServiceUnavailableError,
                openai.error.Timeout,
            ) as error:
                print(error, "\n Retrying in 20s...")
                time.sleep(20)
                tags, score, summary = prompt.summarize(chunks)

            print('Completed Extraction')

            publication = {
                'date': str(date),
                'area': area,
                'url': url,
                'type': type,
                'summary': summary,
                'tags': tags,
                'score': score
            }

            print('Publication Created')
            print(publication)

            loader.json_loader(publication)
            print("Loaded to json")
        else:
            print(f"Area: {area} not in Areas Of Interest.")
        print('***************')

if __name__ == "__main__":
    main()
