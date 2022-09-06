import pytest

from subscriber.base import ZMQHandler
from subscriber.hashblock import HashBlockHandler


class ZMQ_RCVMocker:
    def __init__(self, return_value):
        self.return_value = return_value

    async def recv_multipart(self):
        return self.return_value


@pytest.fixture
def zmq_recv_mocker():
    yield ZMQ_RCVMocker


@pytest.fixture
def zmq_handler():
    handler = ZMQHandler()
    yield handler


@pytest.fixture
def hashblock_handler():
    handler = HashBlockHandler()
    yield handler
