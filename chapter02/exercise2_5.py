from chapter02.TenArmedTestbed import Bandit


# # for figure 2.2
def epsilonGreedy(nBandits, time, epsilon):
    bandits.append([Bandit(epsilon, sampleAverages=True) for _ in range(0, nBandits)])
    bestActionCounts, averageRewards = banditSimulation(nBandits, time, bandits)
    return bestActionCounts, averageRewards


bestActionCounts, averageRewards = epsilonGreedy(2000, 1000)

global figureIndex
plt.figure(figureIndex)
figureIndex += 1
for eps, counts in zip(epsilons, bestActionCounts):
    plt.plot(counts, label='epsilon = '+str(eps))
plt.xlabel('Steps')
plt.ylabel('% optimal action')
plt.legend()
plt.figure(figureIndex)
figureIndex += 1
for eps, rewards in zip(epsilons, averageRewards):
    plt.plot(rewards, label='epsilon = '+str(eps))
plt.xlabel('Steps')
plt.ylabel('average reward')
plt.legend()
