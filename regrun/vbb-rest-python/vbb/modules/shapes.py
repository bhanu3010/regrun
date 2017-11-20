from basemodule import BaseModule


class Shapes(BaseModule):
    """Module to invoke shapes API of VBB REST"""
    def __init__(self, requester=None):
        super(Shapes, self).__init__(requester)

    def get_shape(self, id=None):
        data, headers = self.r.request('shapes/{}'.format(id))

        return data
