def collatztags(input):
	keys = {'a': 'bc', 'b': 'a', 'c': 'aaa'}
	while len(input) > 1:
		input = input[2:]+keys[input[0]]
		print(input)

if __name__ == "__main__":
	inputs = ['aaa', 'aaaaa', 'aaaaaaa']
	for input in inputs:
		collatztags(input)