inputs = [12348765, 1234, 1243, 234765, 19000, 4321]

def next(input):
	inputList = list(str(input))
	inputListReverse = inputList[::-1]

	for i in range(len(inputListReverse)-1):
		if (inputListReverse[i] > inputListReverse[i+1]):
			for m in sorted(inputListReverse[:i+2]):
				if m > inputListReverse[i+1]:
					inputListReverse.insert(i+2, m)
					inputListReverse.remove(m)
					inputListReverse = sorted(inputListReverse[:i+1])[::-1]+inputListReverse[i+1:]
					break
			break
	return ''.join(inputListReverse[::-1])

for input in inputs:
	print(next(input))