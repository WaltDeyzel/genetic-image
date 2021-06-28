from cv2 import cv2
import numpy as np
from numpy import random as npR
from PIL import Image 
import math
import random


class Genome:

    def __init__(self, dna):
        self.dna = dna
        self.fit = 1
        self.fitness_ratio = 0
    
    def getDNA(self):
        return(self.dna)
    
    def getFitness(self):
        return(self.fit)
    
    def getFitnessRatio(self):
        return(self.fitness_ratio)

    def showImage(self):
        self.img = Image.fromarray(self.dna)
        self.img.show()
    
    def closeImage(self):
        self.img.close()
    
    def fitness(self, row_target, col_target):
        dna = np.square(self.dna)
        row_score = np.sum(dna, axis=1)
        col_score = np.sum(dna, axis=0)

        score = 0
        for i in range(len(row_target)):
            score += abs(row_score[i] - row_target[i])
        for i in range(len(col_target)):
            score += abs(col_score[i] - col_target[i])
        
        self.fit = 1/score

    def mutate(self):
        
        for _ in range(3):
            c = random.randint(0, len(self.dna[0])-1)
            r = random.randint(0, len(self.dna)-1)
            # print(r, c)
            self.dna[r,c] = np.random.choice([0, 255], 1)
            #random.randint(0, 255)
        

    def setFitness2Population(self, total):
        self.fitness_ratio = self.fit/total


if __name__ == "__main__":
    # img = Image.open('grad.png')
    
    # img.show()

    img = cv2.imread('grad.png',0)
    dna = np.asarray(img)

    # print(img.size)
    # print(len(dna))
    # print(dna)
    dna[0][0] = 143
    dna = np.asarray(img)
    
    # print(dna)
    img = Image.fromarray(dna)
    img.save('greyscale2.png')

    Ted = Genome(dna)