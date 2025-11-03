import numpy as np


def relu(x):
    return (x > 0) * x


def relu2deriv(output):
    return output > 0


def learn(streetlights, walk_vs_stop):
    np.random.seed(1)

    alpha = 0.2
    hidden_size = 4
    weights_0_1 = 0
    weights_1_2 = 0

    # fill out

    return weights_0_1, weights_1_2


if __name__ == '__main__':
    streetlights = np.array([[1, 0, 1],
                             [0, 1, 1],
                             [0, 0, 1],
                             [1, 1, 1]])

    walk_vs_stop = np.array([[1, 1, 0, 0]]).T

    weights_0_1 = np.array([
        [-0.16595599, 0.91056768, -0.99977125, -0.90023925],
        [-0.70648822, - 0.92794391, -0.62747958, 0.89703458],
        [-0.20646505, - 0.03308324, -0.16161097, 0.00237016]])

    weights_1_2 = np.array([[-0.5910955],
                            [1.13962134],
                            [-0.94522481],
                            [1.11023793]])

    result_0_1, result_1_2 = learn(streetlights, walk_vs_stop)
    assert np.allclose(result_0_1, weights_0_1)
    assert np.allclose(result_1_2, weights_1_2)
