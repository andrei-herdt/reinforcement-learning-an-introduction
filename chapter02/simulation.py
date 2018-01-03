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
