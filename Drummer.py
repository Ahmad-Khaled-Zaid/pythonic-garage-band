from Musician import Musician


class Drummer(Musician):
    def __init__(self, name):
        super().__init__(self)

        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    @staticmethod
    def get_instrument():
        return "drums"

    @staticmethod
    def play_solo():
        return "rattle boom crash"
