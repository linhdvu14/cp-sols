''' D. Not Adding
https://codeforces.com/contest/1627/problem/D
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

def gcd(a, b):
    '''assume a, b >= 0'''
    if a < b: a, b = b, a
    while b > 0: a, b = b, a % b
    return a


def solve(N, A):
    MAX = max(A) 
    known = [False] * (MAX+1)  # faster than set
    for a in A: known[a] = True
    res = 0

    for d in range(1, MAX):
        if known[d]: continue

        # d can be added if d is gcd of some subset of A
        g = -1
        for md in range(2*d, MAX+1, d):
            if not known[md]: continue
            g = md if g == -1 else gcd(g, md)
            if g == d: break
        
        if g == d: res += 1

    return res


def main():
    N = int(input())
    A = list(map(int, input().split()))
    out = solve(N, A)
    output(f'{out}\n')


if __name__ == '__main__':
    main()

