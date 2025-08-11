''' C. Minimum Extraction
https://codeforces.com/contest/1607/problem/C
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def solve(N, nums):
	nums.sort()
	res = nums[0]
	d = -nums[0]
	for i in range(1, N):
		cur = nums[i] + d
		res = max(res, cur)
		d -= cur	
	return res


def main():
	T = int(input())
	for _ in range(T):
		N = int(input())
		nums = list(map(int, input().split()))
		out = solve(N, nums)
		output(str(out) + '\n')


if __name__ == '__main__':
	main()

