from flask_sqlalchemy import SQLAlchemy

from redis import Redis
from rq import Queue
from rq_scheduler import Scheduler
from datetime import datetime

db = SQLAlchemy()

connection = Redis()

queue = Queue("default", connection=connection)
scheduler = Scheduler(connection=connection, queue=queue)

