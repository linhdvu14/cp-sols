''' G. Banquet Preparations 1
https://codeforces.com/contest/1607/problem/G
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

# let taster eat m_i of fish from each dish (a_i, b_i)
# then balance is SUM_i (a_i - b_i) + N*M - 2*SUM_i m_i
# --> select m_i s.t. 
# * SUM_i m_i is as close as possible to (SUM_i (a_i - b_i) + N*M) / 2
# * max(0, M-b_i) <= m_i <= min(a_i, M)

def solve(N, M, masses):
	res_a = [0]*N
	target = 0
	cands = []
	for i, (a, b) in enumerate(masses):
		target += a - b + M
		lo, hi = max(0, M-b), min(a, M)
		if lo > 0:
			res_a[i] += lo
			hi -= lo
			target -= 2*lo
		cands.append((hi, i))
	cands.sort(reverse=True)

	for a, i in cands:
		if target <= 0: break
		ma = min(a, target//2)
		res_a[i] += ma
		target -= 2*ma

	print(abs(target))
	for ma in res_a:
		print(f'{ma} {M-ma}')


def main():
	T = int(input())
	for _ in range(T):
		_ = input()
		N, M = list(map(int, input().split()))
		masses = [tuple(map(int, input().split())) for _ in range(N)]
		solve(N, M, masses)


if __name__ == '__main__':
	main()

