#Batch Input Logic(Multiple inputs on the same layer)
import numpy as np
inputs=[[2.0,4.0,5.0,6.0],[1.4, 2.5, 3.2, 1.2],[0.4, 5.2, 6.3, 1.0]] #  3 Batches
weights=[[6.5, 4.5, -0.5, 2.0],[2.4, 4.5, 1.5, 0.4],[-0.5,1.3, 0.1, -2.1]]
biases = [2, 1, 0]
output = []
output = np.dot(inputs, np.array(weights).T) + biases
print(output)