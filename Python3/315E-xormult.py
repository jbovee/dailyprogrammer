inputs = ['1 2', '9 0', '6 1', '3 3', '2 5', '7 9', '13 11', '5 17', '14 13', '19 1', '63 63'] 

def xormul(a, b):
    result, i = 0, 1
    while i <= b:
        result = result ^ (a * i * (b & i) // i)
        i *= 2
    return result

for a, b in (map(int, input.split()) for input in inputs):
	print('{}@{}={}'.format(a,b,xormul(a,b)))