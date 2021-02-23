import operator
from Genome import Genome
import numpy as np
from numpy import random as npR
from Generate import generate, shuffle, revert
from cv2 import cv2 
from Selection import rouletteSelection, tournamentSelection
from Crossover import crossover
from PIL import Image 

def show():

    dna = best_genome.getDNA()
    image = revert(data, n, dna)
    img = Image.fromarray(image)
    img.show()


if __name__ == "__main__":
    n = 32
    img = cv2.imread('images.png',0)
    data = np.asarray(img)
    r, c = data.shape
    r = int(r/n)*n
    c = int(c/n)*n
    data = data[0:r, 0:c]
    
    key = generate(data, n)
    print(key.shape)
    # Row and Col sum data from original image. 
    # Is used in the fitness function of the genome.
    key = np.square(key)
    row_score = np.sum(key, axis=1)
    col_score = np.sum(key, axis=0)

    population_total = 100
    mutation_rate = 0.35
    crossover_rate = 1
    
    population = []
    best_genome = None

    for _ in range(population_total):
        scramble = shuffle(key)
        population.append(Genome(scramble))

    for i in range(1000000):
        population_fitness = 0
        
        for genome in population:
            genome.fitness(row_score, col_score)
            population_fitness += genome.getFitness()
        
        for genome in population:
            genome.setFitness2Population(population_fitness)

        # sorted_population = sorted(population, key=operator.attrgetter('fitness_ratio'))
        # sorted_population.reverse()
        sorted_population = population.copy()
        best_genome = max(population, key=operator.attrgetter('fit'))
        if i%10000 == 0:
            print('Gen:', i, '--> ', round(1/best_genome.getFitness()))
            show()
        if round(1/best_genome.getFitness()) <= 200:
            print('Done')
            break
        population.clear()
        population.append(best_genome)
        

        while len(population) < population_total:

            new_genome = tournamentSelection(sorted_population)
            option_2 = tournamentSelection(sorted_population)

            if npR.uniform() < crossover_rate:
                dna_1, dna_2 = crossover(new_genome, option_2)
                new_genome = Genome(dna_1)
                new_genome_2 = Genome(dna_2)
                population.append(new_genome_2)

            if npR.uniform() < mutation_rate:
                new_genome.mutate()

            population.append(new_genome)
        
    show()

print('Complete')