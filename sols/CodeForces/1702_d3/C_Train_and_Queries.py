''' C. Train and Queries
https://codeforces.com/contest/1702/problem/C
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

# for int dict key
from random import randrange
RAND = randrange(1 << 62)
def conv(x): return x ^ RAND

INF = float('inf')

# -----------------------------------------

def solve(N, Q, A, queries):
    first, last = {}, {}
    for i, a in enumerate(A):
        a ^= RAND
        if a not in first: first[a] = i
        last[a] = i

    res = ['NO'] * Q
    for i, (l, r) in enumerate(queries):
        l ^= RAND
        r ^= RAND
        if l not in first or r not in first: continue
        if first[l] <= last[r]: res[i] = 'YES'

    return res


def main():
    T = int(input())
    for _ in range(T):
        _ = input()
        N, Q = list(map(int, input().split()))
        A = list(map(int, input().split()))
        queries = [list(map(int, input().split())) for _ in range(Q)]
        out = solve(N, Q, A, queries)
        print(*out, sep='\n')


if __name__ == '__main__':
    main()

