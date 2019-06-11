"""
Test of
- throttle.web.MasterServer
- throttle.web.SlaveClient
"""

import logging
import os
import socket
import sys

CURRENT_PATH = os.path.split(os.path.realpath(__file__))[0]  # noqa
sys.path.append(os.path.join(CURRENT_PATH, '..'))  # noqa

from throttle.controller import MockController
from throttle.web import MasterServer, SlaveClient

logging.getLogger().setLevel(logging.INFO)

server = MasterServer(controller_clz=MockController)
server.start()

server_port = server.port


def server_test():
    # ping test
    s = socket.socket()
    s.connect(('127.0.0.1', server_port))
    s.send(b'throttle::ping')
    print(s.recv(1024))

    # regist test
    for _ in range(5):
        s = socket.socket()
        s.connect(('127.0.0.1', server_port))
        s.send(b'throttle::regist::key1::{"test_key": "test_value"}')
        print(s.recv(1024))

    # run test
    for _ in range(5):
        s = socket.socket()
        s.connect(('127.0.0.1', server_port))
        s.send(b'throttle::admit::key1')
        print(s.recv(1024))


def client_test():
    client = SlaveClient(port=server_port)

    # ping test
    print('Client ping: ', client.ping())

    # regist test
    for _ in range(5):
        print('Client regist: ', client.regist('key2', {'test_key': 'test_value'}))

    # run test
    for _ in range(5):
        print('Client admit: ', client.admit('key2'))


if __name__ == '__main__':
    print('----- Server Test -----')
    server_test()
    print('\n----- Client Test -----')
    client_test()
