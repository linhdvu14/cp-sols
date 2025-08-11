''' A. Gamer Hemose
https://codeforces.com/contest/1592/problem/A
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode() if str
output = sys.stdout.write


def solve(N, H, nums):
	nums.sort(reverse=True)
	mx1, mx2 = nums[0], nums[1]
	times, rem = divmod(H, mx1 + mx2)
	times *= 2
	if rem==0: return times
	if rem <= mx1: return times+1
	return times+2


def main():
	T = int(input())
	for _ in range(T):
		N, H = list(map(int, input().split()))
		nums = list(map(int, input().split()))
		out = solve(N, H, nums)
		output(str(out) + '\n')

if __name__ == '__main__':
    main()