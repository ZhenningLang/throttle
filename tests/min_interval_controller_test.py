import logging
import os
import sys
import time

CURRENT_PATH = os.path.split(os.path.realpath(__file__))[0]  # noqa
sys.path.append(os.path.join(CURRENT_PATH, '..'))  # noqa

from throttle.controller import MinIntervalController
from throttle.web import MasterServer, SlaveClient

logging.getLogger().setLevel(logging.INFO)

server = MasterServer(controller_clz=MinIntervalController)
server.start()

server_port = server.port


client = SlaveClient(port=server_port)

# regist & first call
print('Client regist: ', client.regist('key', {'min_interval': 0.5}))  # 0.5 s
print('First call: ', client.admit('key'))

# fast call
for _ in range(3):
    print('Fast call admit: ', client.admit('key'))
    time.sleep(0.1)

# slow call
for _ in range(3):
    time.sleep(0.5)
    print('Slow call admit: ', client.admit('key'))
