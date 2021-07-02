# Genetic-Image-Reconstruction

In this project I deployed a genetic algorithm to reconstruct an image using only the pixel sum of the row and collums. This method worked really well for very basic shapes but failed when the image contained too much detail. A better method for capturing image date should be used or amore data should be captured with the current implimentation to improve results. 

## Dependencies
### Imports
  - cv2 
  - PIL
  - numpy 
  - matplotlib.pyplot 
  - time
  - operator
  
## How to use

  Supply the program with an image you would like to compress.
  
  ```
  img = cv2.imread('dot.png', 0)
  ```
   
 Select the resolution you want to capture. 
 
  ```
  n = 64 
  ```
  The following parameters can be toggled.
   ```
   population_total = 250     
   mutation_rate    = 0.45    
   crossover_rate   = 1       
   ```
