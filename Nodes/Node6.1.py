# SoftMax Activation
'''
1) Exponenetial of each value to make it positive
2) normalise the values
'''
import math
import numpy as np
layer_outputs= [[4.8, 1.21, 2.385], 
                [8.9, -1.81, 0.2],
                [1.41, 1.051, 0.026]]
layer_outputs = layer_outputs - np.max(layer_outputs, axis=1, keepdims=True)
print("New LayerOutput is")
print(layer_outputs)
exp_values = np.exp(layer_outputs)
print(exp_values)
print(np.sum(layer_outputs, axis = 1, keepdims=True))
norm_values = exp_values/np.sum(exp_values, axis=1, keepdims=True)
print(norm_values)