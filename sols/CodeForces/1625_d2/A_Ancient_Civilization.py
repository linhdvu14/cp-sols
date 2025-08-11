''' A. Ancient Civilization
https://codeforces.com/contest/1625/problem/A
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

def solve(N, L, X):
    cnt = [0]*30
    for i in range(30):
        for x in X:
            if (x >> i) & 1:
                cnt[i] += 1
    
    res = 0
    for c in cnt[::-1]:
        res <<= 1
        if c > N // 2: res |= 1

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, L = list(map(int, input().split()))
        X = list(map(int, input().split()))
        out = solve(N, L, X)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

