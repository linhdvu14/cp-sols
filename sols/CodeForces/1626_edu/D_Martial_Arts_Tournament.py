''' D. Martial Arts Tournament
https://codeforces.com/contest/1626/problem/D
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
    C = [0]*(N+1)
    for a in A: C[a] += 1
    C = [c for c in C if c > 0]
    N = len(C)

    pref, suff = [0], [0]
    for c in C: pref.append(pref[-1]+c)
    for c in C[::-1]: suff.append(suff[-1]+c)

    # for each possible rounded left/right sum
    # include as many prefix/suffix eles as possible
    left_idx = [0]*32
    for i in range(32):
        target = 1 << i
        res, lo, hi = -1, 0, N
        while lo <= hi:
            mi = (lo+hi) // 2
            if pref[mi] <= target:
                res = mi
                lo = mi + 1
            else:
                hi = mi - 1
        left_idx[i] = res

    right_idx = [0]*32
    for i in range(32):
        target = 1 << i
        res, lo, hi = -1, 0, N
        while lo <= hi:
            mi = (lo+hi) // 2
            if suff[mi] <= target:
                res = mi
                lo = mi + 1
            else:
                hi = mi - 1
        right_idx[i] = res
    
    # check each possible left/right sum combination
    res = INF
    for li in range(32):
        for ri in range(32):
            lt, rt = left_idx[li], right_idx[ri]
            cand = (1<<li) - pref[lt] + (1<<ri) - suff[rt]
            if lt + rt > N: cand += pref[lt] - pref[N - rt]
            rem = max(pref[N] - pref[lt] - suff[rt], 0)
            cand += get_next_power_of_two(rem) - rem
            res = min(res, cand)

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        out = solve(N, A)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

