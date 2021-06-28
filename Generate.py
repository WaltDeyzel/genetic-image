import random
import numpy as np
from cv2 import cv2 
from PIL import Image 
from datetime import datetime

def generate(data, n):

    rows, cols = data.shape

    dx = int(cols / n) 
    # number of squares along Y axis
    ver = int(rows / dx)
    # number of squares along X axis
    hor = n
    
    empty = np.zeros((ver, hor), dtype=int)
    
    start_x = 0
    start_y = 0

    for r in range(ver):
        for c in range(hor):
            empty[r][c] =  int(np.sum(np.sum(data[start_y:start_y+dx, start_x:start_x+dx]))/(dx**2))
            start_x += dx
            if start_x >= cols:
                start_x = 0
        start_y += dx
        
    
    return empty

def revert(data, n, dna):

    rows, cols = data.shape
    dx = int(cols / n) 

    empty = np.zeros((rows, cols))

    start_x = 0
    start_y = 0

    for row in dna:
        for val in row:
            empty[start_y:start_y+dx, start_x:start_x+dx] = val
            start_x += dx
            if start_x >= cols:
                start_x = 0
        start_y += dx
        if start_y >= rows:
            break

    return empty
    
            
def shuffle(grid):
    #print(datetime.now())
    # random.seed(datetime.now())
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            grid[row,col] = np.random.choice([0, 255], 1)
            #random.randint(0,256)#int(npR.uniform()*256)
    
    return grid


def revert2(data, n, dna):

    rows, cols = data.shape

    hor = int(cols/n)
    ver = int(rows/n)

    empty = np.zeros((rows, cols))
    row_no = 0
    col_no = 0
    
    y = 0

    for i in range(rows):
        y += 1
        for a in range(cols):
            
            if y % ver == 0:
                row_no += 1
                y = 0
                if row_no == n:
                    break

            if a % (hor-1) == 0 and a != 0:
                col_no += 1
                if col_no == n:
                    col_no = 0
            if row_no == n:
                break
            empty[i, a] = dna[row_no, col_no]
        if row_no == n:
            break
    return empty

def generate2(data, n): 
    
    rows, cols = data.shape

    hor = int(cols/n)
    ver = int(rows/n)
    m = int(rows/ver)
    empty = np.zeros((n, m), dtype=int)
    bins = np.zeros((n,), dtype=int)
   
    x = 0
    y = 0
    bin_no = 0
    row_no = 0
    
    for row in data:
        total = 0
        for val in row:
            total += val
            x += 1
            if x % (hor) == 0:
                if bin_no > n-1:
                    break
                bins[bin_no] +=  total
                bin_no += 1  
                x = 0  
                total = 0
        bin_no = 0
        y += 1
        if y % (ver) == 0:
            col_no = 0
            for val in bins:
                avg = val/(hor*ver)
                empty[row_no, col_no] = int(avg)
                col_no += 1
            row_no += 1
            bins = np.zeros((n,), dtype=int)
        
    return empty

if __name__ == "__main__":
    n = 64
    img = cv2.imread('dot.png',0)
    #grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
    (thresh, img) = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    data = np.asarray(img)
    rows, cols = data.shape

    dx = int(cols / n) 
    cols = n*dx
    m = int(rows / dx)
    rows = m*dx
    
    data = data[0:rows, 0:cols]
    print(data.shape)
    # cv2.imshow('',img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    

    dna = generate(data, n)
    #dna = shuffle(dna)
    dna = revert(data, n, dna)
    img = Image.fromarray(dna)
    img.show()