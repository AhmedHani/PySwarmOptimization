__author__ = 'Ahmed Hani Ibrahim'
from bat_algorithm_package import bat_algorithm

t = bat_algorithm.BatAlgorithm(200, 2)
r = t.optimize(0.0, 600)

print(r)

print(1 + r[0]**2 + r[1]**2)