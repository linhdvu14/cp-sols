''' Power Sum
https://www.codechef.com/JAN222A/problems/POWSUM
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug')

if DEBUG:
    from inspect import currentframe, getframeinfo
    from re import search

def debug(*args):
    if not DEBUG: return
    frame = currentframe().f_back
    s = getframeinfo(frame).code_context[0]
    r = search(r"\((.*)\)", s).group(1)
    vnames = r.split(', ')
    var_and_vals = [f'{var}={val}' for var, val in zip(vnames, args)]
    prefix = f'{currentframe().f_back.f_lineno:02d}: '
    print(f'{prefix}{", ".join(var_and_vals)}')


INF = float('inf')

# -----------------------------------------

def get_next_power_of_two(n):
	'''return smallest power of 2 that's >= n'''
	if n == 0: return 1
	if n & (n-1) == 0: return n
	while n & (n-1) != 0:  # clear lowest set bit, until only 1 bit left
		n = n & (n-1)
	return n << 1


def solve(N, A):
    mn, mni, total = A[0], 0, 0
    for i, a in enumerate(A):
        if a < mn: mn, mni = a, i
        total += a
    
    if bin(total).count('1') == 1:
        print(0)
    else:    
        new_total = get_next_power_of_two(total)
        x = (new_total - total + mn) // mn
        print(1)
        print(1, x)
        print(mni+1)


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        solve(N, A)


if __name__ == '__main__':
    main()

