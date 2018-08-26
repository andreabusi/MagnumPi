from flask import Flask
from config import Config
from redis import Redis
import rq

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config.from_object(Config)
app.redis = Redis.from_url(app.config['REDIS_URL'])
app.task_queue = rq.Queue(app.config['QUEUE_BACKGROUND_TASKS'], connection=app.redis)


from app import routes