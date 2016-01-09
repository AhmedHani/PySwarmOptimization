__author__ = 'Ahmed Hani Ibrahim'

import matplotlib.pyplot as plt


class Pair(object):
    x = int
    y = int

    def __init__(self, x, y):
        self.x = x
        self.y = y

index = 'A'

class Bird():
    position = []
    velocity = []
    bestPosition = []
    currentFitness = float
    bestFitness = float
    x, y = [], []

    def __repr__(self):
        return repr((self.position, self.velocity, self.bestPosition, self.currentFitness))


    def printOutput(self):
        global index
        out = ""
        out += "Birds Statistics\n"
        out += "=====================\n"
        out += (index + " ")
        index = chr(ord(index) + 1)
        out += "Bird Current Position: "

        for i in range(0, len(self.position)):
            out += (str(self.position[i]) + " ")

        out += "\n"
        out += "Bird Current Fitness: "
        out += str(self.currentFitness)
        out += "\n"
        out += "Velocity: "

        for i in range(0, len(self.velocity)):
            out += (str(self.velocity[i]) + " ")

        out += "\n"
        out += "Best Solution: "

        for i in range(0, len(self.bestPosition)):
            out += (str(self.bestPosition[i]) + " ")

        out += "\n"
        out += "Best Fitness: "
        out += str(self.bestFitness)
        out += "\n"

        out += "====================="

        self.x.append(self.bestPosition[0])
        self.y.append(self.bestPosition[1])

        return out

    def showData(self):
        plt.plot(self.x, self.y, marker='*', linestyle='--', color='aqua')
        plt.show()