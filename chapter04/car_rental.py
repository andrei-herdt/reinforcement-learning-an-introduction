import numpy as np

def probability(next_state, state, action):
    return 1/20/20

def reward(next_state, state):
    return 1

def policy_evaluation():
    value_function = np.zeros(20 * 20)
    policy = np.zeros(20 * 20)
    eps = 1
    delta = 0
    gamma = 0.9
    # while (delta < eps):
    #     delta = 0
    for state,value in np.ndenumerate(value_function):
        for next_state, value in np.ndenumerate(value_function):
            v = value
            value_function[state] += probability(next_state, state, policy[state])*(reward(next_state, state)+gamma*value_function[next_state])
            # delta = max(delta, abs(v-state.value)
    print(value_function)

# def learn_policy():
#     policy_iteration()
