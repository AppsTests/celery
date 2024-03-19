from celery import Celery
from dotenv import load_dotenv
import os

load_dotenv()

RABBITMQ_USERNAME = os.getenv('RABBITMQ_USERNAME')
RABBITMQ_PASSWORD = os.getenv('RABBITMQ_PASSWORD')
RABBITMQ_HOST = os.getenv('RABBITMQ_HOST')
RABBITMQ_PORT = os.getenv('RABBITMQ_PORT')
RABBITMQ_DBNAME = os.getenv('RABBITMQ_DBNAME')

app = Celery('tasks', broker=f'pyamqp://{RABBITMQ_USERNAME}:{RABBITMQ_PASSWORD}@{RABBITMQ_HOST}:{RABBITMQ_PORT}/{RABBITMQ_DBNAME}')

@app.task
def add(x, y):
    return x + y
