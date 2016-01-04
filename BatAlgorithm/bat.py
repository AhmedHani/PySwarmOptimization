__author__ = 'Ahmed Hani Ibrahim'


class Bat(object):
    __id = int
    __position = []
    __velocity = []
    __best_position = []

    def print_bat_data(self):
        print("Bat number: ", self.__id)
        print("Bat current position", self.__position)
        print("Bat current velocity", self.__velocity)
        print("Bat best position", self.__best_position)


