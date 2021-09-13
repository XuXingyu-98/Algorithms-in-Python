
def prova(n, denoms):
	ways = [0 for _ in range(n + 1)]
	ways[0] = 1

	for denom in denoms:
		for amount in range(1, n + 1):
			if denom <= amount:
				ways[amount] += ways[amount - denom]

	return ways[-1]

print(prova(100, [1, 2, 5]))



