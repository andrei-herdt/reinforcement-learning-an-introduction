import numpy as np

# def policy(state):
#     return policy_vec(state.id)

# def policy_iteration():

def policy_evaluation():
    value_function = np.zeros(20 * 20)
    policy = np.zeros(20 * 20)
    eps = 1
    delta = 0
    # while (delta < eps):
    #     delta = 0
    for state,value in np.ndenumerate(value_function):
        v = value
        value_function(state) = np.sum(p(s_next, r, s, pi))*(r+gamma*s_next.value)
        delta = max(delta, abs(v-state.value)

# def learn_policy():
#     policy_iteration()
