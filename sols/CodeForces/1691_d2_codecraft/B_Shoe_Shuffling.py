''' B. Shoe Shuffling
https://codeforces.com/contest/1691/problem/B
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
    pos = {}
    for i, a in enumerate(A):
        if a not in pos: pos[a] = []
        pos[a].append(i)

    res = [-1] * N 
    for idx in pos.values():
        if len(idx) == 1: return [-1]
        for i in range(len(idx)):
            res[idx[i]] = idx[(i + 1) % len(idx)] + 1

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        out = solve(N, A)
        print(*out)


if __name__ == '__main__':
    main()

