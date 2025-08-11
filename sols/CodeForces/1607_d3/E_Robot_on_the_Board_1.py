''' E. Robot on the Board 1
https://codeforces.com/contest/1607/problem/E
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def solve(R, C, moves):
	pmnr = pmnc = mnr = mxr = mnc = mxc = 0
	r = c = 0
	for m in moves:
		if m == 'L': c -= 1
		if m == 'R': c += 1
		if m == 'U': r -= 1
		if m == 'D': r += 1
		mnr = min(mnr, r)
		mxr = max(mxr, r)
		mnc = min(mnc, c)
		mxc = max(mxc, c)
		if mxr-mnr >= R or mxc-mnc >= C: break
		pmnr, pmnc = mnr, mnc
	return (abs(pmnr), abs(pmnc))


def main():
	T = int(input())
	for _ in range(T):
		R, C = list(map(int, input().split()))
		moves = input().decode().strip()
		r, c = solve(R, C, moves)
		output(f'{r+1} {c+1}\n')


if __name__ == '__main__':
	main()

