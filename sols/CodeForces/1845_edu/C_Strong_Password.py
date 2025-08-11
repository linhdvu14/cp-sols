''' C. Strong Password
https://codeforces.com/contest/1845/problem/C 
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def debug(*args):   
    if os.environ.get('debug') in [None, '0']: return
    from inspect import currentframe, getframeinfo
    from re import search
    frame = currentframe().f_back
    s = getframeinfo(frame).code_context[0]
    r = search(r"\((.*)\)", s).group(1)
    vnames = r.split(', ')
    var_and_vals = [f'{var}={val}' for var, val in zip(vnames, args)]
    prefix = f'{currentframe().f_back.f_lineno:02d}: '
    print(f'{prefix}{", ".join(var_and_vals)}')

INF = float('inf')

# -----------------------------------------
from bisect import bisect_left

def solve(S, M, L, R):
    S = list(map(int, list(S)))
    L = list(map(int, list(L)))
    R = list(map(int, list(R)))

    pos = [[] for _ in range(10)]
    for i, c in enumerate(S): pos[c].append(i)

    cur = 0
    for l, r in zip(L, R):
        mx = -1
        for c in range(l, r + 1):
            i = bisect_left(pos[c], cur)
            if i == len(pos[c]): return 'YES'
            mx = max(mx, pos[c][i])
        cur = mx + 1

    return 'NO'


def main():
    T = int(input())
    for _ in range(T):
        S = input().decode().strip()
        M = int(input())
        L = input().decode().strip()
        R = input().decode().strip()
        res = solve(S, M, L, R)
        print(res)


if __name__ == '__main__':
    main()

