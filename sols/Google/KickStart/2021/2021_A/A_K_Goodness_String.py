''' K-Goodness String 
https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068cca3
'''
def solve(N,K,S):
	count = 0
	for i in range(N//2):
		if S[i] != S[-1-i]: count += 1
	return abs(K-count)


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())

	for t in range(T):
		N,K = list(map(int,stdin.readline().strip().split()))
		S = stdin.readline().strip()
		out = solve(N,K,S)
		print('Case #{}: {}'.format(t+1, out))


if __name__ == '__main__':
	main()