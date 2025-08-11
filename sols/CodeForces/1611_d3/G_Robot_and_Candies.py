''' G. Robot and Candies
https://codeforces.com/contest/1611/problem/G
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

INF = float('inf')
from bisect import bisect_right

def lis(nums):
    # dp[i] = min num that can be end value of an inc subsequence of length i
    # note dp is strictly increasing
    dp = [INF]*(len(nums)+1)  
    dp[0] = -INF
    
    for num in nums:
        j = bisect_right(dp, num)  # first number > num
        if dp[j-1] < num < dp[j]:  # change first < to <= if longest non-decreasing
            dp[j] = num
    for i, v in enumerate(dp):
        if v < INF:
            res = i
    return res


def solve(R, C, grid):
	# only possible to move from a black cell to a lower black cell
	# so solve separately for black and white 1s
	partitions = [[], []]
	for r in range(R):
		for c in range(C):
			if grid[r][c] == '1':
				partitions[(r+c) % 2].append((r, c))
	
	# dilworth
	# can get to (r, c) if start between (0, c-r) and (0, c+r)
	# so can move from (r1, c1) to (r2, c2) if c2-r2 <= c1-r1 <= c1+r1 <= c2+r2
	# want to minimize num chains / maximize antichain length
	# https://www.quora.com/How-do-I-solve-the-nested-doll-problem-on-SPOJ
	def _solve(ones):
		# left increase, right decrease
		A = [(c-r, -c-r) for r, c in ones]
		A.sort()

		# keep right bounds
		A = [-y for _, y in A]

		# (i+1)-th interval can be nested in i-th interval if A[i+1] <= A[i]
		# so max antichain is longest strictly increasing subsequence
		return lis(A)

	return _solve(partitions[0]) + _solve(partitions[1])


def main():
	T = int(input())
	for _ in range(T):
		input()
		R, C = list(map(int, input().split()))
		grid = [input().decode().strip() for _ in range(R)]
		out = solve(R, C, grid)
		output(f'{out}\n')


if __name__ == '__main__':
	main()

