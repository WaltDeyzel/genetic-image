from Genome import Genome
import operator
from numpy import random as npR
from Crossover import crossover
from Generate import shuffle, generate
from Selection import rouletteSelection, tournamentSelection
import matplotlib.pyplot as plt
import math
from cv2 import cv2
import numpy as np
class Simulate:

    def __init__(self, population_total, crossover_rate, mutation_rate, solution, generations, selection, crossover):
        self.population_total = population_total
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.solution = solution
        self.population = []
        self.generations = generations

        self.crossover = crossover
        self.selection = selection
        self.results = []
    
    def run(self):
        for _ in range(population_total):
            scramble = shuffle(key)
            self.population.append(Genome(scramble))

        for _ in range(100000):
            #print('GENERATION :', i, round(1/population[0].getFitness()))
            population_fitness = 0
            
            for genome in self.population:
                genome.fitness(row_score, col_score)
                population_fitness += genome.getFitness()
            
            for genome in self.population:
                genome.setFitness2Population(population_fitness)

            sorted_population = sorted(self.population, key=operator.attrgetter('fitness_ratio'))
            sorted_population.reverse()
            best = sorted_population[0]
            sorted_population.append(best)
            if 1/best.getFitness() <= 10:
                break
            self.population.clear()
            

            for _ in range(population_total-1):

                new_genome = rouletteSelection(sorted_population)
                option_2 = rouletteSelection(sorted_population)

                if npR.uniform() < crossover_rate:
                    new_genome = Genome(crossover(new_genome, option_2))

                if npR.uniform() < mutation_rate:
                    new_genome.mutate()

                self.population.append(new_genome)



if __name__ == "__main__":

    img = cv2.imread('grad.png',0)
    data = np.asarray(img)
    key = generate(data, 8)

    row_score = np.sum(key, axis=1)
    col_score = np.sum(key, axis=0)

    population_total = 500
    mutation_rate = 0.1
    crossover_rate = 0.5
    simulations = 100

    sim_1 = Simulate(population_total, crossover_rate, mutation_rate, key, simulations, tournamentSelection, crossover)  #BLUE
    

    plt.plot(sim_1.run()) #BLUE
   
    plt.show()