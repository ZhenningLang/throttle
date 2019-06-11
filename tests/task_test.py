import logging
import os
import sys
import time
from multiprocessing import Process

CURRENT_PATH = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(os.path.join(CURRENT_PATH, '..'))

from throttle import task  # noqa

logging.getLogger().setLevel(logging.INFO)


@task(min_interval=0.1)
def foo():
    print(f'In foo: {time.time()}')


def task(cnt=10):
    for _ in range(cnt):
        foo()


for _ in range(5):
    Process(target=task).start()
