''' D1. All are Same
https://codeforces.com/contest/1593/problem/D1
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write


# for all x, y in nums: x - mk = y - nk ---> x - y = (n-m)k
def solve(N, nums):
	def gcd(a, b):  # assume non-neg
		if a<b: a,b = b,a
		while b>0: a,b = b, a%b
		return a

	mn = min(nums)
	nums = [num - mn for num in nums]
	if all(num==0 for num in nums): return -1
	g = nums[0]
	for i in range(1, N):
		g = gcd(g, nums[i])
	return g


def main():
	T = int(input())
	for _ in range(T):
		N = int(input())
		nums = list(map(int, input().split()))
		out = solve(N, nums)
		output(str(out) + '\n')


if __name__ == '__main__':
	main()

