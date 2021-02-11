import operator
from Genome import Genome
import numpy as np
from numpy import random as npR
from Generate import generate, shuffle, revert2
from cv2 import cv2 
from Selection import rouletteSelection, tournamentSelection
from Crossover import crossover
from PIL import Image 


if __name__ == "__main__":
    n = 64
    img = cv2.imread('sthuthi.jpg',0)
    data = np.asarray(img)
    r, c = data.shape
    r = int(r/n)*n
    c = int(c/n)*n
    data = data[0:r, 0:c]

    key = generate(data, n)

    row_score = np.sum(key, axis=1)
    col_score = np.sum(key, axis=0)

    population_total = 300
    mutation_rate = 0.15
    crossover_rate = 1
    
    population = []
    best_genome = None

    for _ in range(population_total):
        scramble = shuffle(key)
        population.append(Genome(scramble))

    for _ in range(250000):
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
        # print(1/best_genome.getFitness())
        if 1/best_genome.getFitness() <= 10:
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
        
    
    dna = best_genome.getDNA()
    image = revert2(data, n, dna)
    img = Image.fromarray(image)
    img.show()

    
        
print('Done')