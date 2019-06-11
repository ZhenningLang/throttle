from typing import Any, Callable, Tuple, Dict


class ThrottleNode:

    def __init__(self):
        self.role = None  # master or slave
        self.master_port = None
        self.join()

    def join(self):
        """ Join local network """
        port, found = self.detect_master()
        if found:
            self.role = 'slave'
            self.master_port = port
        else:
            self.role = 'master'
            self.master_port = port

    def detach(self):
        """ Detach local network
        NOT implemented in current version, which means a mater dying
        """

    def detect_master(self) -> (int, bool):
        """ Detect master node's port
        :return port, found
        """

    def registry(self, fn: Callable, round_seconds: int, max_call_num_in_round: int):
        """ Registry function fn

        :param fn:
        :param round_seconds: Total time of one round of control, unit is in second
        :param max_call_num_in_round: Maximum called times of function fn in one round of control
        :return:
        """

    def run(self, fn: Callable, args: Tuple, kwargs: Dict) -> Any:
        """ Run function fn """
