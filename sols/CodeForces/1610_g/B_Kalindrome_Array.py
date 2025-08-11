''' B. Kalindrome Array
https://codeforces.com/contest/1610/problem/B
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def solve(N, nums):
	def is_palin(rm):
		i, j = 0, N-1
		while i < j:
			if nums[i] == rm:
				i += 1
			elif nums[j] == rm:
				j -= 1
			elif nums[i] == nums[j]:
				i += 1
				j -= 1
			else:
				return False
		return True
	
	i, j = 0, N-1
	while i < j:
		if nums[i] == nums[j]:
			i += 1
			j -= 1
		else:
			return is_palin(nums[i]) or is_palin(nums[j])

	return True


def main():
	T = int(input())
	for _ in range(T):
		N = int(input())
		nums = list(map(int, input().split()))
		out = solve(N, nums)
		print('YES' if out else 'NO')


if __name__ == '__main__':
	main()

