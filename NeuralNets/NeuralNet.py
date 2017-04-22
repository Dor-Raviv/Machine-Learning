import numpy as np


def nonlin(x, deriv=False):
    if (deriv == True):
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))


# input Data

X = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])

# output Data

y = np.array([[0], [1], [1], [0]])

np.random.seed(1)

# synapses - 3 Layers: 2 Synapses

syn0 = 2 * np.random.random((3, 4)) - 1
syn1 = 2 * np.random.random((4, 1)) - 1

# training Step

for j in range(60000):
    layer_0 = X
    layer_1 = nonlin(np.dot(layer_0, syn0))
    layer_2 = nonlin(np.dot(layer_1, syn1))

    layer_2_error = y - layer_2

    if (j % 10000) == 0:
        print("Error: {}".format(np.mean(np.abs(layer_2_error))))

    layer_2_delta = layer_2_error * nonlin(layer_2, deriv=True)
    #     Back propagation

    layer_1_error = layer_2_delta.dot(syn1.T)

    layer_1_delta = layer_1_error * nonlin(layer_1, deriv=True)

    # Update weights (Gradient descent)
    syn1 += layer_1.T.dot(layer_2_delta)
    syn0 += layer_0.T.dot(layer_1_delta)

print("Output After Training")
print(layer_2)
