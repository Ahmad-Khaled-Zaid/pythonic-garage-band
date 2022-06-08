
from Drummer import Drummer
from Bassist import Bassist
from Guitarist import Guitarist


class Band:
    instances = []

    @classmethod
    def to_list(cls):
        return Band.instances

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def play_solos(self):
        solos = []
        for i in self.members:
            solos.append(i.play_solo())
        return solos
