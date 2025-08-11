''' D. Guess the Permutation
https://codeforces.com/contest/1589/problem/D
'''

import functools
import sys
input = sys.stdin.readline  # io.BytesIO(os.read(0,os.fstat(0).st_size)).readline doesn't work
output = functools.partial(print, flush=True)

from math import sqrt

def main():
	T = int(input())
	for _ in range(T):
		N = int(input())

		# total inversions
		output(f'? 1 {N}')
		total = int(input())

		# find right
		right, lo, hi = N, 2, N-1
		while lo <= hi:
			mi = (lo + hi) // 2
			output(f'? 1 {mi}')
			sub = int(input())
			if sub < total:
				lo = mi + 1
			else:
				right = mi
				hi = mi - 1
		
		# find mid
		output(f'? 1 {right-1}')
		offset = total - int(input())
		mid = right - offset

		# find left
		target = 2 * (total - offset*(offset+1) // 2)  # 2 * num left inversions
		lsize = int(sqrt(target))
		if lsize*(lsize-1) > target: lsize -= 1
		if lsize*(lsize-1) < target: lsize += 1
		left = mid - lsize

		output(f'! {left} {mid} {right}')



if __name__ == '__main__':
	main()

