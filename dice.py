from random import randint

class Dice():
    """ The class simulates dices """

    def __init__(self, num_sides=6):
        """ Initialize 6-side dice """
        self.nsides = num_sides
    
    def roll(self):
        """ Return a random value between 1-6 """
        return randint(1, self.nsides)