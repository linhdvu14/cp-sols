''' F. Ideal Farm
https://codeforces.com/contest/1594/problem/F
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

# try to construct the longest unlucky distribution with sum S
# i.e. longest (prefix) array P s.t. 
# * P[0] == 0, P[-1] == S
# * P is strictly increasing
# * P doesn't contain both (x, x+K) for any x
# then ans is NO iff len(P) >= n+1

# for each r=0..K-1, at most x=r, r+2K, r+4K, ... r+(2m)K <= S can be included in P
# so len(P) = SUM_(r=0..K-1) (S-r) // (2K) + 1

def solve(S, N, K):
	if S == K: return 'YES\n'
	sz = S // (2*K) * K + K
	sz -= K - min(1 + S % (2*K), K)   # out of r=0..K-1, the first 1 + S % 2K have (S-r) // (2K) == S // (2K)
	return 'NO\n' if sz >= N+1 else 'YES\n'

def main():
	T = int(input())
	for _ in range(T):
		S, N, K = list(map(int, input().split()))
		out = solve(S, N, K)
		output(out)


if __name__ == '__main__':
	main()

