import os
import json
import datetime

from typing import List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from redis_om import get_redis_connection, JsonModel

from utils.generate_publication import generate_publication

from dotenv import load_dotenv
load_dotenv()


PASSWORD  = os.getenv('REDIS_USER_PASSWORD')
HOST = os.getenv('REDIS_HOST')
PORT = os.getenv('REDIS_PORT')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*'],
)

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


@app.get('/publications/')
def get_all_publications():
    return [format(pk) for pk in Publication.all_pks()]

@app.post('/publication/{id}')
def post_publication(id: int):
    publication = generate_publication(id)
    print(publication['date'], type(publication['date']))
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

def format(pk: str):
    publication = Publication.get(pk)
    return {
        'id': publication.id,
        'date': publication.date,
        'url': publication.url,
        'type': publication.type,
        'summary': publication.summary,
        'tags': publication.tags,
        'score':publication.score
    }