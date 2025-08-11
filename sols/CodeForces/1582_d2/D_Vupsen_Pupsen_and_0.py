''' D. Vupsen, Pupsen and 0
https://codeforces.com/contest/1582/problem/D
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write
 
def solve(N, nums):
	res = []
	for i in range(0, N-1, 2):
		n1, n2 = nums[i], nums[i+1]
		res += [n2, -n1]
	if N % 2 == 1:
		n1, n2, n3 = nums[-3], nums[-2], nums[-1]
		if n2+n3 != 0:
			res = res[:-2] + [n2+n3, -n1, -n1]
		elif n1+n2 != 0:
			res = res[:-2] + [-n3, -n3, n1+n2]
		else:
			res = res[:-2] + [-n2, n1+n3, -n2]
 
	return res
 
 
def main():
	T = int(input())
	for _ in range(T):
		N = int(input())
		nums = list(map(int, input().split()))
		out = solve(N, nums)
		output(' '.join(map(str, out)) + '\n')
 
 
if __name__ == '__main__':
	main()