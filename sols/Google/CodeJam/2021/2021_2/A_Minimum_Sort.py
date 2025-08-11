''' Minimum Sort 
https://codingcompetitions.withgoogle.com/codejam/round/0000000000435915/00000000007dc51c
'''
# python interactive_runner.py python local_testing_tool.py 0 -- python3 a.py

from sys import stdin, stdout, stderr

import functools
print = functools.partial(print, flush=True)


def solve(N):
	for i in range(1,N):
		print(f'M {i} {N}', flush=True)
		j = int(stdin.readline().strip())
		if j > i:
			print(f'S {i} {j}', flush=True)
			_ = int(stdin.readline().strip())
	print('D', flush=True)
	_ = int(stdin.readline().strip())


def main():
	T, N = list(map(int,stdin.readline().strip().split()))
	for t in range(T):
		solve(N)
	
 
if __name__ == '__main__':
	main()