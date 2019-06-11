from typing import Any, Callable, Tuple, Dict

from .configs import PORT_CHOICES
from .controller import MinIntervalController
from .web import MasterServer, SlaveClient


class ThrottleNode:

    def __init__(self):
        self.role = None  # master or slave
        self.master_port = None
        self.master_server_thread = None  # this is not None of only master node
        self.join()

    def join(self):
        """ Join local network """
        port, found = self.detect_master()
        if found:
            self.role = 'slave'
            self.master_port = port
        else:  # try to be the master
            # get file lock
            self.master_server_thread = MasterServer(controller_clz=MinIntervalController)
            self.master_server_thread.start()
            # release file lock
            self.role = 'master'
            self.master_port = port

    def detach(self):
        """ Detach local network
        NOT implemented in current version, which means a mater dying
        """

    # noinspection PyMethodMayBeStatic
    def detect_master(self) -> (int, bool):
        """ Detect master node's port
        :return port, found
        """
        client = SlaveClient(0)
        for port in PORT_CHOICES:
            if client.ping(port):
                return port, True
        else:
            return -1, False

    def registry(self, fn: Callable, **kwargs) -> bool:
        """ Registry function fn """

    def run(self, fn: Callable, args: Tuple, kwargs: Dict) -> Any:
        """ Run function fn """
