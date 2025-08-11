''' F1. Korney Korneevich and XOR (easy version)
https://codeforces.com/contest/1582/problem/F1
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write
 
A = float('inf')
X = 513
 
def solve(nums, N):
	# dp[xor] = min ending val s.t. running XOR is xor
	dp = [A]*X
	dp[0] = -1
 
	for num in nums:
		for xor in range(X):
			if dp[xor] >= num: continue
			dp[num^xor] = min(dp[num^xor], num)
	return [xor for xor in range(X) if dp[xor] < A]
 
 
def main():
	N = int(input())
	nums = list(map(int, input().split()))
	out = solve(nums, N)
	output(str(len(out)) + '\n')
	output(' '.join(map(str, out)) + '\n')
 
if __name__ == '__main__':
	main()