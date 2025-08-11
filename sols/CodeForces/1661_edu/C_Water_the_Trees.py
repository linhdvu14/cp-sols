''' C. Water the Trees
https://codeforces.com/contest/1661/problem/C
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

def solve(N, A):
    res = INF
    mx = max(A)
    for m in [mx, mx + 1]:
        two = one = 0
        for a in A:
            two += (m - a) // 2
            one += (m - a) % 2
        if two - one >= 2:
            t = (two - one + 1) // 3
            one += 2 * t
            two -= t
        if two < one: res = min(res, one * 2 - 1)
        elif two == one: res = min(res, one * 2)
        elif two == one + 1: res = min(res, two * 2)
        else: assert False
    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        out = solve(N, A)
        print(out)


if __name__ == '__main__':
    main()

