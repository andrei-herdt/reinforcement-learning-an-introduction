import numpy as np
import math as math
import matplotlib.pyplot as plt

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
    for ncars_1, ncars_2 in value_function:
        state = (ncars_1, ncars2)
        cars_moved = policy(state)
        # for next_state, value in np.ndenumerate(value_function):
            # v = value
        for cars_rented in range(0,cars_available):
            capacity = total_capacity - cars_available + cars_rented - cars_moved
            for cars_returned in range(0,capacity):
                next_state = cars_available - cars_rented + cars_returned
                value_function[state] += prob_rent_1(cars_rented)*prob_return_1(cars_returned)*(reward(cars_rented)+gamma*value_function[next_state - 1])
        # delta = max(delta, abs(v-state.value)

    print(value_function)
    plt.plot(value_function)
    plt.xlabel('Number cars available')
    plt.ylabel('Value')
    plt.show()

# def learn_policy():
#     policy_iteration()



if __name__ == '__main__':
        policy_evaluation()
