''' C. Grandma Capa Knits a Scarf
https://codeforces.com/contest/1582/problem/C
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write
 
def solve(N, S):
	MAX = float('inf')
	res = MAX
	S = [ord(c)-ord('a') for c in S]
	for i in range(26):
		rm = 0
		lo, hi = 0, N-1
		while lo < hi:
			if S[lo] == S[hi]:
				lo += 1
				hi -= 1
			elif S[lo] == i:
				rm += 1
				lo += 1
			elif S[hi] == i:
				rm += 1
				hi -= 1
			else:
				rm = MAX
				break
		res = min(res, rm)
 
	return res if res < MAX else -1
 
 
def main():
	T = int(input())
	for _ in range(T):
		N = int(input())
		S = input().decode().strip()
		out = solve(N, S)
		output(str(out) + '\n')
 
 
if __name__ == '__main__':
	main()