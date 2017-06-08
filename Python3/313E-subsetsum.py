inputs = [[1, 2, 3], [-5, -3, -1, 2, 4, 6], [], [-1, 1], [-97364, -71561, -69336, 19675, 71561, 97863], [-53974, -39140, -36561, -23935, -15680, 0]]

def subsetsum(input):
	return any([x for x in input if (-x in input) or (0 in input)])

for input in inputs:
	print('{} -> {}'.format(input, subsetsum(input)))