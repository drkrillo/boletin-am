import os
from datetime import date

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from redis_om import get_redis_connection, HashModel

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

class Publication(HashModel):
    id: int
    date: date
    url: str
    type: str
    tags: list
    score: int

    class Meta:
        database = redis


@app.get('/publication/{id}')
def get_publication(id: int):
    return Publication.get(id)

@app.post('/publication/{id}')
def post_publication(id: int):
    publication = generate_publication(id)
    return Publication.save()