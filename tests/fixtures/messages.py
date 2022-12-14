import pytest


@pytest.fixture
def hashblock_message():
    yield [
        b"hashblock",
        b"\x00\x00\x00\x00\x00\x00\x00\x1e\xb9>\x1f)Q\xeb\x8e\xd0\x0f\xdf.\xcf\x12\x047\xaf[\x84\x05\xe5\x88\xc4\x9f\x80",
        b";\x00\x00\x00",
    ]
