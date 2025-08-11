''' C. Binary String
https://codeforces.com/contest/1680/problem/C
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') not in [None, '0']

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


def solve_binsearch(S):
    idx = [i for i, c in enumerate(S) if c == '1']
    if not idx or len(idx) == len(S): return 0

    def is_ok(cost):
        one = len(idx) - cost  # min num ones in remaining interval
        for i in range(one - 1, len(idx)):
            zero = idx[i] - idx[i - one + 1] + 1 - one
            if zero <= cost: return True
        return False

    res, lo, hi = -1, 0, len(idx)
    while lo <= hi:
        mi = (lo + hi) // 2
        if is_ok(mi):
            res = mi 
            hi = mi - 1
        else:
            lo = mi + 1

    return res
            

def solve_2pointers(S):
    idx = [i for i, c in enumerate(S) if c == '1']
    if not idx or len(idx) == len(S): return 0

    res, l, r = INF, 0, 0
    while r < len(idx):
        one_out = len(idx) - (r - l + 1)
        zero_in = idx[r] - idx[l] + 1 - (r - l + 1)
        res = min(res, max(one_out, zero_in))
        if one_out >= zero_in: r += 1
        else: l += 1
    
    return res


solve = solve_2pointers

def main():
    T = int(input())
    for _ in range(T):
        S = input().decode().strip()
        out = solve(S)
        print(out)


if __name__ == '__main__':
    main()

