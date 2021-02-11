from random import randint
import random
from numpy import random as npR

def crossover(option_1, option_2):

    dna_1 = option_1.getDNA()
    dna_2 = option_2.getDNA()
    copy = dna_1.copy()
    n = int(len(dna_1)/2)
    m = int(len(dna_1[0])/2)

    copy[0:n,0:n] = dna_2[0:n,0:n]
    dna_2[0:n,0:n] = dna_1[0:n,0:n]
    child_1 = copy
    child_2 = dna_2
    
    
    return(child_1, child_2)



if __name__ == "__main__":
    pass