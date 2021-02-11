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
    
    def sumRow(self):

        row_score = np.sum(self.dna, axis=1)
        return row_score

    def sumCol(self):

        col_score = np.sum(self.dna, axis=0)
        return col_score
    
    def fitness(self, row_target, col_target):

        row_score = self.sumRow()
        col_score = self.sumCol()

        score = 0
        for i in range(len(row_target)):
            score += abs(row_score[i] - row_target[i])**2
            score += abs(col_score[i] - col_target[i])**2
        
        self.fit = 1/score

    def mutate(self):
        
        for _ in range(5):
            n = random.randint(0, len(self.dna)-1)
            m = random.randint(0, len(self.dna)-1)
            val = random.randint(0, 255)
            self.dna[n,m] = val
        

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

    print(Ted.sumRow())
    print(Ted.sumCol())