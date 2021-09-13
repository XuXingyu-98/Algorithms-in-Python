def minRewards(scores):
    rewards = [1 for _ in scores]
    for i in range(1, len(scores)):
        if scores[i] > scores[i - 1]:
            rewards[i] = rewards[i - 1] + 1
    for i in reversed(range(len(scores) - 1)):
        if scores[i] > scores[i + 1]:
            rewards[i] = max(rewards[i], rewards[i + 1] + 1)
    return sum(rewards)
#another solution

def minRewards(scores):
    rewards = [1 for _ in scores]
    localMinIds = getLocalMinIds(scores)
    for localMinId in localMinIds:
        expandFromLocalMin(localMinId, rewards, scores)
    return sum(rewards)

def getLocalMinIds(scores):
    if len(scores) == 1:
        return [0]
    localMindIds = []
    for i in range(0, len(scores)):
        if i == 0 and scores[i] < scores[i + 1]:
            localMindIds.append(i)
        if i == len(scores) - 1 and scores[i] < scores[i - 1]:
            localMindIds.append(i)
        if i == 0 or i == len(scores) - 1:
            continue
        if scores[i] < scores[i - 1] and scores[i] < scores[i + 1]:
            localMindIds.append(i)
    return localMindIds

def expandFromLocalMin(localMinId, rewards, scores):
    left = localMinId - 1
    while left >= 0 and scores[left] > scores[left + 1]:
        rewards[left] = max(rewards[left], rewards[left + 1] + 1)
        left -= 1
    right = localMinId + 1
    while right < len(scores) and scores[right] > scores[right - 1]:
        rewards[right] = rewards[right - 1] + 1
        right += 1


scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]
print minRewards(scores)