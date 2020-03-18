from Comet import Comet
import random


class CometSpawner:
    def __init__(self, screenwidth, screenheight):
        self.screenwidth = screenwidth
        self.screenheight = screenheight

    def spawn_a_comet(self):
        return Comet(5, random.randint(0, self.screenwidth), random.randint(0, self.screenheight))




