from random import randint
import random
from numpy import random as npR

def rouletteSelection(sorted_population):
    
    x = npR.uniform()
    tot = 0
    for genome in sorted_population:
        tot += genome.getFitnessRatio()
        if(x<=tot):
            return genome 

    return(sorted_population[0])

def tournamentSelection(sorted_population):
    x_1 = int(npR.uniform()*len(sorted_population))
    x_2 = int(npR.uniform()*len(sorted_population))

    option_1 = sorted_population[x_1]
    option_2 = sorted_population[x_2]

    if option_1.getFitness() < option_2.getFitness():
        return option_2
    return option_1


