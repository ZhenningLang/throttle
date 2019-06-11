import logging
import os
import sys
import time
from multiprocessing import Process

CURRENT_PATH = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(os.path.join(CURRENT_PATH, '..'))

from throttle.node import ThrottleNode  # noqa

logging.getLogger().setLevel(logging.INFO)


def foo(node_id):
    print(f'In foo: {time.time()}, node id: {node_id}')


def task(cnt=3):
    node = ThrottleNode()
    print(node.guid, ': ', node.role)
    node.registry(foo, min_interval=0.1)
    for _ in range(cnt):
        node.run(foo, args=(node.guid, ))


for _ in range(5):
    Process(target=task).start()
