import logging
import os
import random
import sys
import time
from multiprocessing import Process

CURRENT_PATH = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(os.path.join(CURRENT_PATH, '..'))

from throttle import task as throttle_task  # noqa

logging.getLogger().setLevel(logging.INFO)


class Foo:

    def __init__(self):
        self.id = random.random()

    @throttle_task(min_interval=0.1)
    def foo(self):
        print(f'In foo: {time.time()}, id: {self.id}')


def task(cnt=10):
    inst = Foo()
    for _ in range(cnt):
        inst.foo()


for _ in range(5):
    Process(target=task).start()
