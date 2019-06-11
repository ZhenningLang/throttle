import os
import sys
# noinspection PyUnresolvedReferences
import time
from threading import Thread

CURRENT_PATH = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(os.path.join(CURRENT_PATH, '..'))

from throttle.lock import DisFileLock, current_timestamp  # noqa

TEST_FILE = 'temp'
TEST_THREAD_NUM = 100


def task(lock: bool):
    for _ in range(10):
        if not lock:
            with open(TEST_FILE, 'r') as f:
                num = int(f.read()) + 1
            print(num)
            with open(TEST_FILE, 'w') as f:
                f.write(str(num))
        else:
            with DisFileLock():
                with open(TEST_FILE, 'r') as f:
                    num = int(f.read()) + 1
                print(num)
                with open(TEST_FILE, 'w') as f:
                    f.write(str(num))


def no_lock_test():
    with open(TEST_FILE, 'w') as f:
        f.write(str(0))
    for _ in range(TEST_THREAD_NUM):
        Thread(target=task, args=(False,)).start()


def lock_test():
    with open('temp', 'w') as f:
        f.write(str(0))
    for _ in range(TEST_THREAD_NUM):
        Thread(target=task, args=(True,)).start()


if __name__ == '__main__':
    # print('----- No lock test -----')
    # no_lock_test()   # fail
    # time.sleep(3)
    print('\n----- Lock test -----')
    lock_test()
