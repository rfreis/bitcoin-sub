import logging

from celery import Celery

from app.settings import PUB_BROKER_URL


logger = logging.getLogger(__name__)


pub_broker = Celery(broker=PUB_BROKER_URL)


def publish_data(task_name, *args):
    logger.info(f"Sending task: {task_name}, args: {args}")
    pub_broker.send_task(name=task_name, args=args)
