import numpy as np


class NeuronLayer():
    def __init__(self, number_of_neurons, number_of_inputs_per_neuron):
        self.synaptic_weights = 2 * np.random.random((number_of_inputs_per_neuron, number_of_neurons)) - 1


class NeuralNetwork():
    def __init__(self, layer1, layer2):
        self.layer1 = layer1
        self.layer2 = layer2

    # The Sigmoid function, which describes an S shaped curve.
    # We pass the weighted sum of the inputs through this function to
    # normalise them between 0 and 1.
    def __sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # The derivative of the Sigmoid function.
    # This is the gradient of the Sigmoid curve.
    # It indicates how confident we are about the existing weight.
    def __sigmoid_derivative(self, x):
        return x * (1 - x)

    # We train the neural network through a process of trial and error.
    # Adjusting the synaptic weights each time.
    def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
        for iteration in range(number_of_training_iterations):
            # Pass the training set through our neural network
            output_from_layer_1, output_from_layer_2 = self.think(training_set_inputs)

            # Calculate the error for layer 2 (The difference between the desired output
            # and the predicted output).
            layer2_error = training_set_outputs - output_from_layer_2
            layer2_delta = layer2_error * self.__sigmoid_derivative(output_from_layer_2)

            # Calculate the error for layer 1 (By looking at the weights in layer 1,
            # we can determine by how much layer 1 contributed to the error in layer 2).
            layer1_error = layer2_delta.dot(self.layer2.synaptic_weights.T)
            layer1_delta = layer1_error * self.__sigmoid_derivative(output_from_layer_1)

            # Calculate how much to adjust the weights by
            layer1_adjustment = training_set_inputs.T.dot(layer1_delta)
            layer2_adjustment = output_from_layer_1.T.dot(layer2_delta)

            # Adjust the weights.
            self.layer1.synaptic_weights += layer1_adjustment
            self.layer2.synaptic_weights += layer2_adjustment

    # The neural network thinks.
    def think(self, inputs):
        output_from_layer1 = self.__sigmoid(
np.dot
(inputs, self.layer1.synaptic_weights))
        output_from_layer2 = self.__sigmoid(
np.dot
(output_from_layer1, self.layer2.synaptic_weights))
        return output_from_layer1, output_from_layer2

    # The neural network prints its weights
    def print_weights(self):
        print("    Layer 1 (4 neurons, each with 3 inputs): ")
        print(self.layer1.synaptic_weights)
        print("    Layer 2 (1 neuron, with 4 inputs)")
        print(self.layer2.synaptic_weights)

neural_network = None

def init():
    global neural_network

    np.random.seed(1)
    num_questions = 7

    # Beschreibt, was die i-te Person jeweils gewaehlt hat
    person_choices = np.array([
        [1, 4, 2, 3, 1, 0, 3],
        [6, 1, 3, 1, 3, 1, 2],
        [2, 5, 1, 3, 2, 1, 8],
        [2, 2, 5, 1, 6, 1, 2]
    ])
    assert person_choices.shape[1] == num_questions

    # Setze neuronales Netzwerk auf
    layer1 = NeuronLayer(12, num_questions * 2)
    layer2 = NeuronLayer(1, 12)
    neural_network = NeuralNetwork(layer1, layer2)

    # Beschreibe die Input-Daten
    training_set_inputs = np.array([
        np.concatenate([person_choices[0], person_choices[2]]),
        np.concatenate([person_choices[1], person_choices[3]]),
        np.concatenate([person_choices[0], person_choices[3]]),
        np.concatenate([person_choices[3], person_choices[0]]),
        np.concatenate([person_choices[2], person_choices[3]]),
        np.concatenate([person_choices[3], person_choices[2]])
    ])
    training_set_outputs = np.array([[0.4, 0.7, 0.9, 0.9, 0.3, 0.3]]).T

    # Trainiere das neuronale Netzwerk
    neural_network.train(training_set_inputs, training_set_outputs, 60000)

def check_match(person_one_choices, person_two_choices):
    global neural_network
    return neural_network.think(np.concatenate([person_one_choices, person_two_choices]))[1]


init()
neural_network.print_weights()

''' if __name__ == "__main__":
    np.random.seed(1)
    num_questions = 5

    # Beschreibt, was die i-te Person jeweils gewaehlt hat
    person_choices = np.array([
        [1, 4, 2, 3, 1],
        [6, 1, 3, 1, 3],
        [2, 5, 1, 3, 2],
        [2, 2, 5, 1, 6]
    ])
    assert person_choices.shape[1] == num_questions

    # Setze neuronales Netzwerk auf
    layer1 = NeuronLayer(12, num_questions * 2)
    layer2 = NeuronLayer(1, 12)
    neural_network = NeuralNetwork(layer1, layer2)

    # Beschreibe die Input-Daten
    training_set_inputs = np.array([
        np.concatenate([person_choices[0], person_choices[2]]),
        np.concatenate([person_choices[1], person_choices[3]]),
        np.concatenate([person_choices[0], person_choices[3]]),
        np.concatenate([person_choices[3], person_choices[0]]),
        np.concatenate([person_choices[2], person_choices[3]]),
        np.concatenate([person_choices[3], person_choices[2]])
    ])
    training_set_outputs = np.array([[0.4, 0.7, 0.9, 0.9, 0.3, 0.3]]).T

    # Trainiere das neuronale Netzwerk
    neural_network.train(training_set_inputs, training_set_outputs, 60000)

    # Validiere die Eingabedaten
    print('Validierung')
    print(neural_network.think(np.concatenate([person_choices[0], person_choices[2]]))[1])
    print(neural_network.think(np.concatenate([person_choices[1], person_choices[3]]))[1])
    print(neural_network.think(np.concatenate([person_choices[0], person_choices[3]]))[1])
    print(neural_network.think(np.concatenate([person_choices[2], person_choices[3]]))[1])

    # Mache weitere Messungen
    print('\nWeitere Messungen')
    print(neural_network.think(np.concatenate([person_choices[1], person_choices[2]]))[1])
    print(neural_network.think(np.concatenate([person_choices[3], person_choices[0]]))[1])
    print(neural_network.think(np.concatenate([person_choices[3], person_choices[2]]))[1])
    '''