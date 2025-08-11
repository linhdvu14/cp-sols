''' Min Max LCM
https://www.codechef.com/SNCK1A21/problems/MINLCM1
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def solve(X, K):
    mn, mx = 2*X, K*X*(K*X-1)
    mn = min(mn, mx)
    print(f'{mn} {mx}')


def main():
	T = int(input())
	for _ in range(T):
		X, K = list(map(int, input().split()))
		solve(X, K)


if __name__ == '__main__':
	main()

