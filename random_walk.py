import random

class RandomWalk():
    """ A class that is used for generating random walk data """

    def __init__(self, num_points = 5000):
        self.num_points = num_points
        
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        x_direction = random.choice([1, -1])
        x_distance = random.choice([0, 1, 2, 3, 4, 5])
        x_step = x_direction * x_distance
        
        y_direction = random.choice([1, -1])
        y_distance = random.choice([0, 1, 2, 3, 4, 5])
        y_step = y_direction * y_distance

        if x_step == 0 and y_step == 0:
            return False

        next_x = self.x_values[-1] + x_step
        next_y = self.y_values[-1] + y_step

        self.x_values.append(next_x)
        self.y_values.append(next_y)

        return True
