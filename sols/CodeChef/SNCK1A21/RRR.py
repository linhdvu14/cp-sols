''' Round Robin Ranks
https://www.codechef.com/SNCK1A21/problems/RRR
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

# should win ranks K+1..N and even with ranks 1..K-1
def solve(N, K):
    res = ((N-K) + (K-1) // 2) * 2
    print(res)


def main():
	T = int(input())
	for _ in range(T):
		N, K = list(map(int, input().split()))
		solve(N, K)


if __name__ == '__main__':
	main()

