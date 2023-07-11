import os
import json
import datetime

from typing import List

from redis_om import get_redis_connection, JsonModel

from utils.generate_publication import generate_publication

from dotenv import load_dotenv
load_dotenv()


PASSWORD  = os.getenv('REDIS_USER_PASSWORD')
HOST = os.getenv('REDIS_HOST')
PORT = os.getenv('REDIS_PORT')
INDEX =288652

redis = get_redis_connection(
    host=HOST,
    port=PORT,
    password=PASSWORD,
    decode_responses=True,
)


class Publication(JsonModel):
    id: int
    date: datetime.date
    url: str
    type: str
    summary: str
    tags: List
    score: int

    class Meta:
        database = redis

def post_publication(id: int):
    publication = generate_publication(id)
    publication = Publication(
        id=publication['id'],
        date=publication['date'],
        url=publication['url'],
        type=publication['type'],
        summary=publication['summary'],
        tags=publication['tags'],
        score=publication['score'],
    )
    return publication.save()

if __name__ == '__main__':
    print('Starting scraping...')
    enabled = True
    index = INDEX
    while enabled:
        publication = post_publication(index)
        print(f'{index} Done.')
        index += 1
