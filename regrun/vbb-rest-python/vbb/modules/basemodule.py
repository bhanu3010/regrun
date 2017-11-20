from ..requester import Requester


class BaseModule(object):
    """Base module for all VBB modules"""
    def __init__(self, requester=None):
        if requester:
            self.r = requester
        else:
            self.r = Requester()
