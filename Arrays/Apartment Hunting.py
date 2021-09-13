def apartmentHunting(blocks, reqs):
    minDistancesFromBlocks = list(map(lambda req: getMinDistances(blocks, req), reqs))
    maxDistancesAtBlocks = getMaxDistancesAtBlocks(minDistancesFromBlocks, blocks)
    return getIdMinValue(maxDistancesAtBlocks)


def getMinDistances(blocks, req):
    minDistances = [0 for block in blocks]
    closestReqId = float("inf")
    for i in range(len(blocks)):
        if blocks[i][req]:
            closestReqId = i
        minDistances[i] = distanceBetween(i, closestReqId)
    for i in reversed(range(len(blocks))):
        if blocks[i][req]:
            closestReqId = i
        minDistances[i] = min(minDistances[i], distanceBetween(i, closestReqId))
    return minDistances

def distanceBetween(a, b):
    return abs(a - b)

def getMaxDistancesAtBlocks(minDistancesFromBlocks, blocks):
    maxDistancesAtBlocks = [0 for block in blocks]
    for i in range(len(blocks)):
        minDistancesAtBlock = list(map(lambda distances: distances[i], minDistancesFromBlocks))
        maxDistancesAtBlocks[i] = max(minDistancesAtBlock)
    return maxDistancesAtBlocks

def getIdMinValue(array):
    minId = 0
    minValue = float("inf")
    for i in range(len(array)):
        current = array[i]
        if current < minValue:
            minId = i
            minValue = current
    return minId


blocks = [
    {
      "gym": True,
      "office": False,
      "pool": False,
      "school": True,
      "store": False
    },
    {
      "gym": False,
      "office": False,
      "pool": False,
      "school": False,
      "store": False
    },
    {
      "gym": False,
      "office": True,
      "pool": False,
      "school": True,
      "store": False
    },
    {
      "gym": False,
      "office": True,
      "pool": False,
      "school": False,
      "store": False
    },
    {
      "gym": False,
      "office": False,
      "pool": False,
      "school": False,
      "store": True
    },
    {
      "gym": True,
      "office": True,
      "pool": False,
      "school": False,
      "store": False
    },
    {
      "gym": False,
      "office": False,
      "pool": True,
      "school": False,
      "store": False
    },
    {
      "gym": False,
      "office": False,
      "pool": False,
      "school": False,
      "store": False
    },
    {
      "gym": False,
      "office": False,
      "pool": False,
      "school": False,
      "store": False
    },
    {
      "gym": False,
      "office": False,
      "pool": False,
      "school": True,
      "store": False
    },
    {
      "gym": False,
      "office": False,
      "pool": True,
      "school": False,
      "store": False
    }
  ]

reqs = ["gym", "pool", "school", "store"]

print apartmentHunting(blocks, reqs)