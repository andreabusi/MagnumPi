import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guest'
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'

    QUEUE_BACKGROUND_TASKS = 'magnumpi-tasks'
