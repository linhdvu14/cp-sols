''' A. Luntik and Concerts
https://codeforces.com/contest/1582/problem/A
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

# always possible to make any sum 0..s:
# * greedily use 3-units until not possible
#   * if remain = 1 or 2: solved
#   * if run out of 3-units, greedily use 2-units until not possible:
#      * if remain = 1: solved
#      * if run out of 2-units, greedily use 1-units

# in general, a collection of >= 1 unit each from: a_1 < a_2 < ... < a_n
# can make any sum from 0..sum(collection) if for any a_i, any value in 0..a_i - 1
# can be constructed using <= 1 unit each from a_1 < a_2 < ... < a_(i-1)

def solve(a, b, c):
	s = a + 2*b + 3*c
	return s % 2

def main():
	T = int(input())
	for _ in range(T):
		a, b, c = list(map(int, input().split()))
		out = solve(a, b, c)
		output(str(out) + '\n')
 
 
if __name__ == '__main__':
	main()