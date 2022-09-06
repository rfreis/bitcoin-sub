import pytest


@pytest.mark.asyncio
async def test_process_hashblock(mocker, hashblock_handler, hashblock_message):
    mock_publisher = mocker.patch("subscriber.hashblock.publish_data")

    await hashblock_handler.process_message(*hashblock_message)

    mock_publisher.assert_called_once_with(
        "task_name",
        "000000000000001eb93e1f2951eb8ed00fdf2ecf120437af5b8405e588c49f80",
    )
