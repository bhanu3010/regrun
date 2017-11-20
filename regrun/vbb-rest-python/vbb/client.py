from .base import Base
from .modules.journeys import Journeys
from .modules.lines import Lines
from .modules.logos import Logos
from .modules.maps import Maps
from .modules.radar import Radar
from .modules.shapes import Shapes
from .modules.locations import Locations
from .modules.stations import Stations


class VBBService(Base):
    """VBBService client"""
    def __init__(self):
        super(VBBService, self).__init__()
        self.journeys = Journeys(requester=self.requester)
        self.locations = Locations(requester=self.requester)
        self.lines = Lines(requester=self.requester)
        self.logos = Logos(requester=self.requester)
        self.maps = Maps(requester=self.requester)
        self.radar = Radar(requester=self.requester)
        self.shapes = Shapes(requester=self.requester)
        self.stations = Stations(requester=self.requester)
