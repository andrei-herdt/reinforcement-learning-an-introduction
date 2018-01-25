import numpy as np
import math as math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import pdb

def prob_return_1(number_cars):
    llambda = 3
    return math.pow(llambda, number_cars)/math.factorial(number_cars)*math.exp(-llambda)

def prob_return_2(number_cars):
    llambda = 2
    return math.pow(llambda, number_cars)/math.factorial(number_cars)*math.exp(-llambda)

def prob_rent_1(number_cars):
    llambda = 3
    return math.pow(llambda, number_cars)/math.factorial(number_cars)*math.exp(-llambda)

def prob_rent_2(number_cars):
    llambda = 4
    return math.pow(llambda, number_cars)/math.factorial(number_cars)*math.exp(-llambda)

def policy(state):
    return 0

def reward(cars_rented):
    return 10*cars_rented

def policy_evaluation():
    value_function = np.zeros((20,20))
    eps = 1
    delta = 0
    gamma = 0.9
    # while (delta < eps):
    #     delta = 0
    total_capacity = 20
    for ncars, value in np.ndenumerate(value_function):
        state = ncars
        cars_moved = policy(state)
        # for next_state, value in np.ndenumerate(value_function):
            # v = value
        for cars_rented_1 in range(0,ncars[0]):
            for cars_rented_2 in range(0,ncars[1]):
                capacity_1 = total_capacity - ncars[0] + cars_rented_1 - cars_moved
                capacity_2 = total_capacity - ncars[1] + cars_rented_2 + cars_moved
                for cars_returned_1 in range(0,capacity_1):
                    for cars_returned_2 in range(0,capacity_2):
                        next_state = (state[0] - cars_rented_1 + cars_returned_1, state[1] - cars_rented_2 + cars_returned_2)
                        value_function[ncars[0], ncars[1]] += prob_rent_1(cars_rented_1)*prob_rent_2(cars_rented_2)*prob_return_1(cars_returned_1)*prob_return_2(cars_returned_2)*(reward(cars_rented_1+cars_rented_2)+gamma*value_function[next_state[0] - 1, next_state[1] - 1])
            # delta = max(delta, abs(v-state.value)

    pdb.set_trace()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    xaxis = np.linspace(1,20,1)
    yaxis = np.linspace(1,20,1)
    ax.plot_surface(value_function)
    plt.xlabel('Number cars available 1')
    plt.ylabel('Number cars available 2')
    plt.zlabel('Expected reward')
    plt.show()

# def learn_policy():
#     policy_iteration()



if __name__ == '__main__':
        policy_evaluation()
