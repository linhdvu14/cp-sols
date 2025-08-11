''' Alien Generator 
https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435c44/00000000007ec1cb
'''
from math import sqrt

def solve(G):
	res = 0
	ub = int(sqrt(2*G))+10
	for d in range(ub):
		a = 2*G-d*(d+1)
		b = 2*(d+1)
		k, r = divmod(a,b)
		if r==0 and k>0: res += 1
	return res

def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())

	for t in range(T):
		G = int(stdin.readline().strip())
		out = solve(G)
		print('Case #{}: {}'.format(t+1, out))


if __name__ == '__main__':
	main()
