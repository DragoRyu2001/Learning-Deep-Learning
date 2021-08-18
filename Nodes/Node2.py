#Single Layer Logic(3 Nodes) with single Input
import numpy as np
inputs=[2.0,4.0,5.0,6.0]
weights=[[6.5, 4.5, -0.5, 2.0],[2.4, 4.5, 1.5, 0.4],[-0.5,1.3, 0.1, -2.1]]
biases = [2, 1, 0]
output = []
output = np.dot(weights, inputs) + biases
print(output)