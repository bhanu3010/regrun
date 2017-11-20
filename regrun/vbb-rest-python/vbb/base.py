from .requester import Requester


class Base(object):
    """Base class used to initialize requester"""
    def __init__(self):
        self.requester = Requester()
