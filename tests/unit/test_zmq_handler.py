import pytest


@pytest.mark.asyncio
async def test_handle(mocker, zmq_recv_mocker, hashblock_message, zmq_handler):
    zmq_handler.zmq_socket = zmq_recv_mocker(hashblock_message)
    mock_run = mocker.patch("subscriber.base.asyncio.run")
    mock_process_message = mocker.patch("subscriber.base.ZMQHandler.process_message")
    await zmq_handler.handle()

    assert mock_run.call_count == 1
    mock_process_message.assert_called_once_with(
        b"hashblock",
        b"\x00\x00\x00\x00\x00\x00\x00\x1e\xb9>\x1f)Q\xeb\x8e\xd0\x0f\xdf.\xcf\x12\x047\xaf[\x84\x05\xe5\x88\xc4\x9f\x80",
        "59",
    )


def test_start(mocker, zmq_handler):
    mock_run = mocker.patch("subscriber.base.asyncio.run", side_effect=Exception())
    mock_stop = mocker.patch("subscriber.base.ZMQHandler.stop")
    mock_setup = mocker.patch("subscriber.base.ZMQHandler.setup")
    mock_handle = mocker.patch("subscriber.base.ZMQHandler.handle")
    zmq_handler.start()

    assert mock_setup.call_count == 1
    assert mock_run.call_count == 1
    assert mock_stop.call_count == 1
    assert mock_handle.call_count == 1
