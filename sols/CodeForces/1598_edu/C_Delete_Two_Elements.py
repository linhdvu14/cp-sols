''' C. Delete Two Elements
https://codeforces.com/contest/1598/problem/C
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def solve(N, nums):
	target, rem = divmod(2*sum(nums), N)
	if rem != 0: return 0
	res = 0
	cnt = {}
	for num in nums:
		res += cnt.get(target-num, 0)
		cnt[num] = cnt.get(num, 0) + 1
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

