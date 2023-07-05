import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection

from dotenv import load_dotenv
load_dotenv()


PASSWORD  = os.getenv('REDIS_USER_PASSWORD')


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*'],
)

redis = get_redis_connection(
    host='redis-19817.c90.us-east-1-3.ec2.cloud.redislabs.com',
    port=19817,
    password=PASSWORD,
    decode_responses=True,
)