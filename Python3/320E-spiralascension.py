import numpy as np
import math

def main():
	sizes = range(1,10)
	for n in sizes:
		print(generate_spiral(n))

def generate_spiral(n):
	empty = np.zeros(n**2, dtype=np.uint8).reshape(n,n)
	vals = [x for x in range(1,(n**2)+1)]
	indices = get_spiral_indices(n)
	for val,ind in zip(vals,indices):
		empty[ind[0]][ind[1]] = val
	return empty

def get_ring_indices(startx,starty,n):
	xind = [0]*(n-1) + [x for x in range(n-1)] + [n-1]*(n-1) + [x for x in range(1,n)][::-1]
	xind = [x+startx for x in xind]
	yind = [y for y in range(n-1)] + [n-1]*(n-1) + [y for y in range(1,n)][::-1] + [0]*(n-1)
	yind = [y+starty for y in yind]
	return(list(zip(xind,yind)))

def get_spiral_indices(n):
	finalIndices = []
	ncopy = n
	startx, starty = 0, 0
	while (ncopy > 0):
		if ncopy == 1: finalIndices += [(math.floor(n/2), math.floor(n/2))]
		else: finalIndices += get_ring_indices(startx, starty, ncopy)
		ncopy = ncopy-2
		startx, starty = startx + 1, starty + 1
	return finalIndices

if __name__ == "__main__":
	main()