#Batch Input Logic with multiple layers
import numpy as np
inputs=[[2.0,4.0,5.0],
        [1.4, 2.5, 3.2],
        [0.4, 5.2, 6.3]] #  3 Batches
#Layer 1
weights=[[6.5, 4.5, -0.5],
        [2.4, 4.5, 1.5],
        [-0.5,1.3, 0.1]]
biases = [2, 1, 0]
#Layer 2
weights2=[[6.5, 4.5, -0.5],
        [2.4, -4.5, 1.5],
        [-0.5,-1.3, 0.1]]
biases2 = [-1, 2, 0]

layer1_output = np.dot(inputs, np.array(weights).T) + biases
layer2_output = np.dot(layer1_output, np.array(weights2).T) + biases2
print(layer2_output)