import pytest

from app import settings


settings.LOGGING["handlers"]["app"] = settings.LOGGING["handlers"]["console"]
settings.LOGGING["handlers"]["messages"] = settings.LOGGING["handlers"]["console"]
settings.PUB_BROKER_URL = "amqp://localhost:6379/0"
settings.HASHBLOCK_TASK_NAME = "task_name"
settings.HASHBLOCK_ZMQ_PORT = "28332"


from .fixtures import *
