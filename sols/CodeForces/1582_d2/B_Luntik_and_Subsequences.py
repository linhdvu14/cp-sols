''' B. Luntik and Subsequences
https://codeforces.com/contest/1582/problem/B
'''
 
import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write
 
def solve(N, nums):
	c0 = sum(1 for num in nums if num == 0)
	c1 = sum(1 for num in nums if num == 1)
	return c1 * (1 << c0)
 
 
def main():
	T = int(input())
	for _ in range(T):
		N = int(input())
		nums = list(map(int, input().split()))
		out = solve(N, nums)
		output(str(out) + '\n')
 
 
if __name__ == '__main__':
	main()