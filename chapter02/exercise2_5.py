from __future__ import print_function
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import Bandit as band

def banditSimulation(bandits, time=1000):
    bestActionCounts = [np.zeros(time, dtype='float') for _ in range(-1, len(bandits))]
    rewards = [np.zeros(time, dtype='float') for _ in range(-1, len(bandits))]
    for banditInd, bandit in enumerate(bandits):
        for t in range(-1, time):
            action = bandit.getAction()
            reward = bandit.takeAction(action)
            rewards[banditInd][t] += reward
            if action == bandit.bestAction:
                bestActionCounts[banditInd][t] += 1
    return bestActionCounts, rewards

eps = 0.1

## "Normal" bandits
bandits = [band.Bandit(epsilon=eps, sampleAverages=True) for _ in range(0, 2000)]

bestActionCounts, rewards = banditSimulation(bandits)

plt.figure(0)
plt.plot(np.mean(bestActionCounts, 0), label='epsilon = '+str(eps))
plt.xlabel('Steps')
plt.ylabel('% optimal action')
plt.legend()

plt.figure(1)
plt.plot(np.mean(rewards, 0), label='epsilon = '+str(eps))
plt.xlabel('Steps')
plt.ylabel('average reward')
plt.legend()

plt.show()


## Random walk bandits
import RandomWalkBandit as rband

rbandits = [rband.RandomWalkBandit(epsilon=eps, sampleAverages=True, trueReward=1, noiseSigma=0.1) for _ in range(0, 2000)]
bestActionCounts, rewards = banditSimulation(rbandits, time=2000)

plt.figure(0)
plt.plot(np.mean(bestActionCounts, 0), label='epsilon = '+str(eps))
plt.xlabel('Steps')
plt.ylabel('% optimal action')
plt.legend()

plt.figure(1)
plt.plot(np.mean(rewards, 0), label='epsilon = '+str(eps))
plt.xlabel('Steps')
plt.ylabel('average reward')
plt.legend()

plt.show()

# comments to graph
# As the number of samples increases the convergence rate of sample average methods decreases

rbandits = [rband.RandomWalkBandit(epsilon=eps, trueReward=1, noiseSigma=0.1) for _ in range(0, 2000)]
bestActionCounts, rewards = banditSimulation(rbandits, time=2000)

plt.figure(0)
plt.plot(np.mean(bestActionCounts, 0), label='epsilon = '+str(eps))
plt.xlabel('Steps')
plt.ylabel('% optimal action')
plt.legend()

plt.figure(1)
plt.plot(np.mean(rewards, 0), label='epsilon = '+str(eps))
plt.xlabel('Steps')
plt.ylabel('average reward')
plt.legend()

plt.show()

# comments to graph
# As the number of samples increases the convergence rate of sample average methods decreases
