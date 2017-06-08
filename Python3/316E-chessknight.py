import itertools
from itertools import combinations_with_replacement as c_w_r
from random import randint

moves = [x for x in list(itertools.permutations([1,2,-1,-2], 2)) if abs(x[0]) != abs(x[1])]

def knight_path(x, y):
	n = 0
	while n > -1:
		combs = list(c_w_r(moves,n))
		for comb in combs:
			if sum([c[0] for c in comb]) == x and sum([c[1] for c in comb]) == y:
				return(n)
		n += 1

def main():
	lw, hi = (-20, 20)
	goals = [' '.join([str(randint(lw, hi)) for x in range(2)]) for x in range(10)]
	for goal in goals:
		x, y = [x for x in map(int, goal.split())]
		print('Goal: {}\n{}'.format(goal, knight_path(x,y)))

if __name__ == "__main__":
	main()