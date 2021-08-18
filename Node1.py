#Single Node Logic
inputs=[2.0,4.0,5.0,6.0]
weights=[6.5, 4.5, -0.5, 2.0]
bias = 2
output = 0
for input, weight in zip(inputs, weights):
    output = output + input*weight
    print(str(input) + " * " + str(weight) + " + ")
print(bias)
output += bias

print(output)