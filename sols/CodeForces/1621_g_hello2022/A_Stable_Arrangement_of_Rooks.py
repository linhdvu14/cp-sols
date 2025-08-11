''' A. Stable Arrangement of Rooks
https://codeforces.com/contest/1621/problem/A
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') is not None

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

def solve(N, K):
    if N == 1: return [['R']]
    if K > (N+1)//2: return [['-1']]
    
    res = [['.']*N for _ in range(N)]
    c = 0
    for i in range(N):
        if c < K and i % 2 == 0:
            res[i][i] = 'R'
            c += 1
    return res


def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        out = solve(N, K)
        for row in out: print(''.join(row))


if __name__ == '__main__':
    main()

