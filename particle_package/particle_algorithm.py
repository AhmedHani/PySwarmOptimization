__author__ = 'Ahmed Hani Ibrahim'


import Globals
from bird import Bird
import random
from math import exp, pow, fabs


class PSO():
    birdsFlock = []
    bestSolution = []
    bestFitness = 0.0

    def initializeBirds(self):
        self.birdsFlock = [Bird() for i in range(0, Globals.NUM_OF_BIRDS)]
        self.bestSolution = [0.0 for i in range(0, Globals.DIMENSION)]
        self.bestFitness = 1.0
        for bird in range(len(self.birdsFlock)):
            randPositions = [0.0 for i in range(0, Globals.DIMENSION)]
            randVelocity = [0.0 for i in range(0, Globals.DIMENSION)]

            for i in range(0, randPositions.__len__()):
                randPositions[i] = (Globals.MAXIMUM_X - Globals.MINIMUM_X) * random.random() + Globals.MINIMUM_X
                randVelocity[i] = (Globals.MAXIMUM_X * 0.1 - Globals.MINIMUM_X * 0.1) * random.random() + Globals.MINIMUM_X

            fitness = self.objectiveFunction(randPositions)

            self.birdsFlock[bird].velocity = randVelocity
            self.birdsFlock[bird].bestPosition = randPositions
            self.birdsFlock[bird].bestFitness = fitness
            self.birdsFlock[bird].currentFitness = fitness
            self.birdsFlock[bird].position = randPositions

            if self.birdsFlock[bird].currentFitness < self.bestFitness:
                self.bestFitness = self.birdsFlock[bird].currentFitness
                self.bestSolution[0] = self.birdsFlock[bird].position[0]
                self.bestSolution[1] = self.birdsFlock[bird].position[1]

    @classmethod
    def objectiveFunction(self, x):
        #testing function found on Internet
        # (2.0 + (x[0]) + (x[1])) Success!
        # (8.0 + x[0] * x[0] + x[1] * x[1]) Success!
        trueTheta = 2.0
        res = 2.0 + x[0] * x[0] + x[1] + x[0]

        return (res - trueTheta) * (res - trueTheta)

    def solve(self):
        for it in range(1, Globals.NUM_OF_ITERATIONS):

            for bird in range(self.birdsFlock.__len__()):
                #update bird's velocity
                r1 = random.random()
                r2 = random.random()
                self.birdsFlock[bird].velocity[0] = (Globals.INSERTIA_WEIGHT * self.birdsFlock[bird].velocity[0]) + \
                                                    (Globals.GLOBAL_WEIGHT * r1 * (self.birdsFlock[bird].bestPosition[0] - self.birdsFlock[bird].position[0])) + \
                                                    (Globals.LOCALE_WEIGHT * r2 * (self.bestSolution[0] - self.birdsFlock[bird].position[0]))
                self.birdsFlock[bird].velocity[1] = (Globals.INSERTIA_WEIGHT * self.birdsFlock[bird].velocity[1]) + \
                                                    (Globals.GLOBAL_WEIGHT * r1 * (self.birdsFlock[bird].bestPosition[1] - self.birdsFlock[bird].position[1])) + \
                                                    (Globals.LOCALE_WEIGHT * r2 * (self.bestSolution[1] - self.birdsFlock[bird].position[1]))

                if self.birdsFlock[bird].velocity[0] < Globals.MINIMUM_V:
                    self.birdsFlock[bird].velocity[0] = Globals.MINIMUM_V
                elif self.birdsFlock[bird].velocity[0] > Globals.MAXIMUM_V:
                    self.birdsFlock[bird].velocity[0] = Globals.MAXIMUM_V

                if self.birdsFlock[bird].velocity[1] < Globals.MINIMUM_V:
                    self.birdsFlock[bird].velocity[1] = Globals.MINIMUM_V
                elif self.birdsFlock[bird].velocity[1] > Globals.MAXIMUM_V:
                    self.birdsFlock[bird].velocity[1] = Globals.MAXIMUM_V

                #end updating

                #update bird's position
                self.birdsFlock[bird].position[0] += self.birdsFlock[bird].velocity[0]
                self.birdsFlock[bird].position[1] += self.birdsFlock[bird].velocity[1]

                if self.birdsFlock[bird].position[0] < Globals.MINIMUM_X:
                    self.birdsFlock[bird].position[0] = Globals.MINIMUM_X
                elif self.birdsFlock[bird].position[0] > Globals.MAXIMUM_X:
                    self.birdsFlock[bird].position[0] = Globals.MAXIMUM_X

                if self.birdsFlock[bird].position[1] < Globals.MINIMUM_X:
                    self.birdsFlock[bird].position[1] = Globals.MINIMUM_X
                elif self.birdsFlock[bird].position[1] > Globals.MAXIMUM_X:
                    self.birdsFlock[bird].position[1] = Globals.MAXIMUM_X
                #end updating


                #update local error
                updatedFitness = self.objectiveFunction(self.birdsFlock[bird].position)
                self.birdsFlock[bird].currentFitness = updatedFitness

                if updatedFitness < self.birdsFlock[bird].bestFitness:
                    self.birdsFlock[bird].bestFitness = updatedFitness
                    self.birdsFlock[bird].bestPosition[0] = self.birdsFlock[bird].position[0]
                    self.birdsFlock[bird].bestPosition[1] = self.birdsFlock[bird].position[1]
                #end update local error

                #update Global Error
                if updatedFitness < fabs(self.bestFitness):
                    self.bestSolution[0] = self.birdsFlock[bird].position[0]
                    self.bestSolution[1] = self.birdsFlock[bird].position[1]
                    self.bestFitness = updatedFitness
                #end update Global Error


                #handling probability of bird death
                dieProb = random.random()

                if dieProb < Globals.DEATH_PROBABILITY:
                    self.birdsFlock[bird].position[0] = fabs(Globals.MAXIMUM_X - Globals.MINIMUM_X) * random.random() +\
                                                        Globals.MINIMUM_X
                    self.birdsFlock[bird].position[1] = fabs(Globals.MAXIMUM_X - Globals.MINIMUM_X) * random.random() +\
                                                        Globals.MINIMUM_X
                    self.birdsFlock[bird].bestPosition[0] = self.birdsFlock[bird].position[0]
                    self.birdsFlock[bird].bestPosition[1] = self.birdsFlock[bird].position[1]
                    self.birdsFlock[bird].currentFitness = self.objectiveFunction(self.birdsFlock[bird].position)
                    self.birdsFlock[bird].bestFitness = self.birdsFlock[bird].currentFitness
                #end handling probability of bird death

        for bird in range(0, len(self.birdsFlock)):
            print(self.birdsFlock[bird].printOutput())

        print("END\n\n")

        print("Solution is: \n")
        print("x = ", self.bestSolution[0])
        print("y = ", self.bestSolution[1])
        print("\n")
        print(self.bestFitness)

        Bird().showData()

    def run(self):
        self.initializeBirds()
        self.solve()