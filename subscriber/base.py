#!/usr/bin/env python3
# Original file: https://github.com/bitcoin/bitcoin/blob/master/contrib/zmq/zmq_sub.py
# Copyright (c) 2014-2021 The Bitcoin Core developers
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import asyncio
import logging
import zmq
import zmq.asyncio
import struct

from app.settings import *


logger_messages = logging.getLogger("messages")


class ZMQHandler:
    task_name = None
    topic = None
    zmq_port = None

    async def process_message(self, topic, body, sequence):
        raise NotImplementedError("Method not implemented")

    async def handle(self):
        topic, body, seq = await self.zmq_socket.recv_multipart()
        logger_messages.debug(f"Topic: {topic} - Body: {body} - Seq: {seq}")
        sequence = "Unknown"
        if len(seq) == 4:
            sequence = str(struct.unpack("<I", seq)[-1])
        asyncio.run(self.process_message(topic, body, sequence))

    def setup(self):
        self.zmq_context = zmq.asyncio.Context()
        self.zmq_socket = self.zmq_context.socket(zmq.SUB)
        self.zmq_socket.setsockopt(zmq.RCVHWM, 1000)
        self.zmq_socket.setsockopt_string(zmq.SUBSCRIBE, self.topic)
        self.zmq_socket.connect(f"tcp://127.0.0.1:{self.zmq_port}")

    def start(self):
        self.setup()
        while True:
            try:
                asyncio.run(self.handle())
            except Exception:
                self.stop()
                break

    def stop(self):
        self.zmq_context.destroy()
