from app.celery import publish_data
from app.settings import HASHBLOCK_TASK_NAME, HASHBLOCK_ZMQ_PORT

from .base import ZMQHandler


class HashBlockHandler(ZMQHandler):
    task_name = HASHBLOCK_TASK_NAME
    topic = "hashblock"
    zmq_port = HASHBLOCK_ZMQ_PORT

    async def process_message(self, topic, body, sequence):
        assert topic.decode() == self.topic
        block_hash = body.hex()
        publish_data(self.task_name, block_hash)
