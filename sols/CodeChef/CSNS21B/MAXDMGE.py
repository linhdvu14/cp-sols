''' Maximum Damage
https://www.codechef.com/CSNS21B/problems/MAXDMGE
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def solve(N, nums):
	res = [0]*N
	res[0] = nums[0] & nums[1]
	res[-1] = nums[-1] & nums[-2]
	for i in range(1, N-1):
		res[i] = max(nums[i] & nums[i-1], nums[i] & nums[i+1]) 
	return res


def main():
	T = int(input())
	for _ in range(T):
		N = int(input())
		nums = list(map(int, input().split()))
		out = solve(N, nums)
		print(' '.join(map(str, out)))


if __name__ == '__main__':
	main()

