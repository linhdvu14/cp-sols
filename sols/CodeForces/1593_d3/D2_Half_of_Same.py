''' D2. Half of Same
https://codeforces.com/contest/1593/problem/D2
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

from math import sqrt

def solve(N, nums):
	thres = N//2
	nums.sort()
	res = 0
	for i in range(thres+1):
		nums2 = [nums[j]-nums[i] for j in range(i, N)]
		if sum(1 for n in nums2 if n==0) >= thres: return -1
		for num in nums2:
			if num == 0: continue
			for k1 in range(1, int(sqrt(nums2[-1])) + 2):
				k2, r = divmod(num, k1)
				if r != 0: continue
				cnt1 = cnt2 = 0
				for num2 in nums2:
					if num2 % k1 == 0: cnt1 += 1
					if num2 % k2 == 0: cnt2 += 1
				if cnt1 >= thres: res = max(res, k1)
				if cnt2 >= thres: res = max(res, k2)
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

