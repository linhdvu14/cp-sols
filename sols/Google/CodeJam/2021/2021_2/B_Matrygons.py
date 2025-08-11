''' Matrygons 
https://codingcompetitions.withgoogle.com/codejam/round/0000000000435915/00000000007dbf06
'''

from math import sqrt

memo = {}

def dp(n, memo):
	if n<2: return 0
	if n in memo: return memo[n]
	res = 1
	for i in range(2, int(sqrt(n))+1):
		m, r = divmod(n, i)
		if r != 0: continue
		res = max(res, dp(m-1,memo)+1, dp(i-1,memo)+1)
	memo[n] = res
	return res

memo = {}
for n in range(3,1001):
	dp(n, memo)


def solve(n):
	res = 1
	for i in range(3, int(sqrt(n))+1):
		m, r = divmod(n, i)
		if r != 0: continue
		res = max(res, dp(m-1,memo)+1, dp(i-1,memo)+1)

	return res


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())

	for t in range(T):
		N = int(stdin.readline().strip())
		out = solve(N)
		print('Case #{}: {}'.format(t+1, out))





if __name__ == '__main__':
	main()