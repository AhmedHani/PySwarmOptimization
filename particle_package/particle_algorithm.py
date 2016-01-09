__author__ = 'Ahmed Hani Ibrahim'

from bird import Bird
import random
from math import fabs
from swarm.algorithm import *


class ParticleAlgorithm(SwarmAlgorithm):
    __minimum_x = -10.0
    __maximum_x = 10.0
    __maximum_v = 100.0
    __minimum_v = -100.0
    __insertia_weight = 0.729
    __locale_weight = 1.49445
    __global_weight = 1.49445
    __death_probability = 0.01  # in range[0, 0.1]

    birds_flock = []
    best_solution = []
    best_fitness = 0.0

    def __init__(self, number_of_objects, number_of_dimensions):
        """

        :param number_of_objects: an integer which determines the number of the bats in the space
        :param number_of_dimensions: an inter which determines the number of the space dimensions
        """
        super(ParticleAlgorithm, self).__init__(number_of_objects, number_of_dimensions)

        self.__init()

    def __init(self):
        self.birds_flock = [Bird() for i in range(0, self._number_of_objects)]
        self.best_solution = [0.0 for i in range(0, self._number_of_dimensions)]
        self.best_fitness = 1.0

        for bird in range(len(self.birds_flock)):
            rand_positions = [0.0 for i in range(0, self._number_of_dimensions)]
            rand_velocity = [0.0 for i in range(0, self._number_of_dimensions)]

            for i in range(0, rand_positions.__len__()):
                rand_positions[i] = (self.__maximum_x - self.__minimum_x) * random.random() + self.__minimum_x
                rand_velocity[i] = (self.__maximum_x * 0.1 - self.__minimum_x * 0.1) * random.random() + self.__maximum_x

            fitness = self.cost_function(rand_positions)

            self.birds_flock[bird].velocity = rand_velocity
            self.birds_flock[bird].best_position = rand_positions
            self.birds_flock[bird].best_fitness = fitness
            self.birds_flock[bird].current_fitness = fitness
            self.birds_flock[bird].position = rand_positions

            if self.birds_flock[bird].current_fitness < self.best_fitness:
                self.best_fitness = self.birds_flock[bird].current_fitness
                self.best_solution[0] = self.birds_flock[bird].position[0]
                self.best_solution[1] = self.birds_flock[bird].position[1]

    def cost_function(self, features):
        true_theta = 2.0
        res = 2.0 + features[0] * features[0] + features[1] + features[0]

        return (res - true_theta) * (res - true_theta)

    def optimize(self, target_error, number_of_iterations):
        for it in range(1, number_of_iterations):
            for bird in range(self.birds_flock.__len__()):
                r1 = random.random()
                r2 = random.random()

                for i in range(0, self._number_of_dimensions):
                    self.birds_flock[bird].velocity[i] = (self.__insertia_weight * self.birds_flock[bird].velocity[i]) + \
                                                    (self.__global_weight * r1 * (self.birds_flock[bird].best_position[i] - self.birds_flock[bird].position[i])) + \
                                                    (self.__locale_weight * r2 * (self.best_solution[i] - self.birds_flock[bird].position[i]))

                    if self.birds_flock[bird].velocity[i] < self.__minimum_v:
                        self.birds_flock[bird].velocity[i] = self.__minimum_v
                    elif self.birds_flock[bird].velocity[i] > self.__maximum_v:
                        self.birds_flock[bird].velocity[i] = self.__maximum_v

                #end updating

                #update bird's position
                self.birds_flock[bird].position[i] += self.birds_flock[bird].velocity[i]

                if self.birds_flock[bird].position[i] < self.__maximum_x:
                    self.birds_flock[bird].position[i] = self.__minimum_x
                elif self.birds_flock[bird].position[i] > self.__maximum_x:
                    self.birds_flock[bird].position[i] = self.__maximum_x
                #end updating


                #update local error
                updated_fitness = self.cost_function(self.birds_flock[bird].position)
                self.birds_flock[bird].current_fitness = updated_fitness

                if updated_fitness < self.birds_flock[bird].best_fitness:
                    self.birds_flock[bird].best_fitness = updated_fitness
                    self.birds_flock[bird].best_position[i] = self.birds_flock[bird].position[i]
                #end update local error

                #update Global Error
                if updated_fitness < fabs(self.best_fitness):
                    self.best_solution[i] = self.birds_flock[bird].position[i]
                    self.best_fitness = updated_fitness
                #end update Global Error


                #handling probability of bird death
                dieProb = random.random()

                if dieProb < self.__death_probability:
                    self.birds_flock[bird].position[i] = fabs(self.__maximum_x - self.__maximum_x) * random.random() +\
                                                        self.__maximum_x
                    self.birds_flock[bird].best_position[i] = self.birds_flock[bird].position[i]
                    self.birds_flock[bird].current_fitness = self.cost_function(self.birds_flock[bird].position)
                    self.birds_flock[bird].best_fitness = self.birds_flock[bird].current_fitness

        return self.best_solution