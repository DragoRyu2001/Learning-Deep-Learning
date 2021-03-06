#Batch Input Logic with multiple layers
import numpy as np
np.random.seed(0)
def spiral_data(points, classes):   # This is to generate Random Input Matrix
    X = np.zeros((points*classes, 2))
    y = np.zeros(points*classes, dtype='uint8')
    for class_number in range(classes):
        ix = range(points*class_number, points*(class_number+1))
        r = np.linspace(0.0, 1, points)  # radius
        t = np.linspace(class_number*4, (class_number+1)*4, points) + np.random.randn(points)*0.2
        X[ix] = np.c_[r*np.sin(t*2.5), r*np.cos(t*2.5)]
        y[ix] = class_number
    return X, y

class Layer_Dense:                  # Layer Object
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights + self.biases)

class Activation_ReLU:              # Rectified Linear Activation Function if value <0 => 0 else give value
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)

X ,y = spiral_data(100, 3)          #Generated a Random Dataset
layer1 = Layer_Dense(2, 5)          
activation1 = Activation_ReLU()     
layer1.forward(X)                   #Feeded the Data to Layer 1
print("Layer 1 Output")             
print(layer1.output)
activation1.forward(layer1.output)  #Feeded the Result from layer to ReLU: Rounded off negative numbers to 0
print("Activation")
print(activation1.output)