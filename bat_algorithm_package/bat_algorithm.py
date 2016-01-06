__author__ = 'Ahmed Hani Ibrahim'
from swarm import algorithm
from bat_algorithm_package.bat import Bat
import random as rnd
import math


class BatAlgorithm(algorithm.SwarmAlgorithm):
    __min_frequency = 0
    __max_frequency = 100
    __max_loudness = 1

    __bats_list = [Bat]
    __bats_pulse_frequency = []
    __initial_bats_pulse_rate = []
    __bats_loudness = []

    __best_position = []

    def __init__(self, number_of_objects, number_of_dimensions):
        super(BatAlgorithm, self).__init__(number_of_objects, number_of_dimensions)

        self.__init()

    def __init(self):
        self.__bats_list = [Bat for i in range(self._number_of_objects)]

        for i in range(self._number_of_objects):
            self.__bats_list[i].id = i
            self.__bats_list[i].best_position = [rnd.random() for i in range(self._number_of_dimensions)]
            self.__bats_list[i].new_position = [rnd.random() for i in range(self._number_of_dimensions)]
            self.__bats_list[i].position = [rnd.random() for i in range(self._number_of_dimensions)]
            self.__bats_list[i].velocity = [rnd.random() for i in range(self._number_of_dimensions)]

        self.__bats_pulse_frequency = [
            rnd.random() * ((self.__max_frequency - self.__min_frequency) + self.__min_frequency) for i in
            range(self._number_of_objects)]

        self.__initial_bats_pulse_rate = [rnd.random() * self.__max_loudness for i in range(self._number_of_objects)]

    def optimize(self, target_error, number_of_iterations):
        iteration = 0
        bats_pulse_rate = self.__initial_bats_pulse_rate
        self.__best_position = self.get_best_features()
        error = abs(self.cost_function(self.__best_position))

        while error > target_error and iteration < number_of_iterations:
            self.__update_bats()


    def cost_function(self, features):
        result = 2.0 + features[0] + features[1]
        true_theta = 2.0

        return (result - true_theta) ** 2

    def get_best_features(self):
        min_value_bat_id = -1
        min_value = self.cost_function(self.__bats_list[0].position)

        for i in range(1, self._number_of_objects):
            current_value = self.cost_function(self.__bats_list[i].position)

            if current_value < min_value:
                min_value = current_value
                min_value_bat_id = self.__bats_list[i].id

        return self.__bats_list[min_value_bat_id].position

    def __update_bats(self):
        self.__update_frequency()
        self.__update_velocity()
        self.__update_position()

    def __update_frequency(self):
        for i in range(self._number_of_objects):
            value = self.__min_frequency + rnd.random() * (self.__max_frequency - self.__min_frequency)
            self.__bats_pulse_frequency[i] = value

    def __update_velocity(self):
        for i in range(self._number_of_objects):
            new_velocity = [0.0 for i in range(self._number_of_objects)]
            for j in range(self._number_of_dimensions):
                new_velocity[j] = self.__bats_list[i].velocity[j] + (self.__bats_list[i].position[j] -
                                                                     self.__best_position[j]) * \
                                                                    self.__bats_pulse_frequency[j]
            self.__bats_list[i].velocity = new_velocity

    def __update_position(self):
        for i in range(self._number_of_objects):
            new_position = [0.0 for i in range(self._number_of_objects)]
            for j in range(self._number_of_dimensions):
                new_position[j] = self.__bats_list[i].position[j] + self.__bats_list[i].velocity[j]

            self.__bats_list[i].position = new_position

    def __update_loudness(self, old_loudness):
        alpha = 0.5

        return alpha * old_loudness

    def __update_pulse_rate(self, old_pulse_rate, iteration):
        gamma = 0.3

        return (1 - math.exp(-gamma * iteration)) * old_pulse_rate





