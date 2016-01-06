__author__ = 'Ahmed Hani Ibrahim'

from abc import ABCMeta, abstractmethod


class SwarmAlgorithm(object):
    __metaclass__ = ABCMeta

    def __init__(self, number_of_objects, number_of_dimensions):
        self._number_of_objects = number_of_objects
        self._number_of_dimensions = number_of_dimensions

    @abstractmethod
    def cost_function(self, features):
        pass

    def optimize(self, target_error, number_of_iterations):
        pass

    def get_error(self):
        pass

    def get_best_features(self):
        pass



