''' Roads in Chefland

https://www.codechef.com/COOK118B/problems/CROADS

'''

from math import log2,ceil

def solve(N):
	if not N&(N-1): return -1
	res = 0
	bits = int(ceil(log2(N+1)))
	for b in range(bits):
		size = (N-(1<<b))//(1<<(b+1)) + 1  # num numbers in range 1..N with lowest set bit at b (start at 1<<b, jump with gap 1<<(b+1))
		res += (1<<b)*(size-1)  # intra-group connects to 1<<b
		if b < bits-1: res += (1<<(b+1))  #  inter-group connects to next bigger

	return res



def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())
	for _ in range(T):
		N = int(stdin.readline().strip())
		out = solve(N)
		print(out)


if __name__ == '__main__':
	main()

