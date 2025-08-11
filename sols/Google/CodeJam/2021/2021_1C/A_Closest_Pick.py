''' Closest Pick 
https://codingcompetitions.withgoogle.com/codejam/round/00000000004362d7/00000000007c0f00
'''
def solve(N,K,P):
	P = sorted(list(set(P)))
	res = 0

	got = []
	for l,r in zip(P,P[1:]):
		d = r-l-1
		res = max(res, d/K)
		if d>0: got += [d//2] if d%2==0 else [(d+1)//2]
	if P[0] > 1: got.append(P[0]-1)
	if P[-1] < K: got.append(K-P[-1])
	got.sort(reverse=True)
	if len(got) == 1: res = max(res, got[0]/K)
	if len(got) > 1: res = max(res, (got[0]+got[1])/K)

	return res


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())

	for t in range(T):
		N,K = list(map(int,stdin.readline().strip().split()))
		P = list(map(int,stdin.readline().strip().split()))
		out = solve(N,K,P)
		print('Case #{}: {}'.format(t+1, out))


if __name__ == '__main__':
	main()