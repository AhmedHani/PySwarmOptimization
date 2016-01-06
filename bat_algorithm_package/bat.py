__author__ = 'Ahmed Hani Ibrahim'


class Bat(object):
    id = int
    position = []
    new_position = []
    velocity = []
    best_position = []

    def print_bat_data(self):
        """
        print the bat data
        """
        print("Bat number: ", self.id)
        print("Bat current position", self.position)
        print("Bat current velocity", self.velocity)
        print("Bat best position", self.best_position)


