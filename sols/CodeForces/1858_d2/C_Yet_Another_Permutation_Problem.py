''' C. Yet Another Permutation Problem
https://codeforces.com/contest/1858/problem/C
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
from heapq import heappop, heapify

def solve(N):
    used = [0] * (N + 1)
    h = list(range(1, N + 1))
    heapify(h)

    res = []
    while h:
        x = heappop(h)
        while x <= N and not used[x]:
            res.append(x)
            used[x] = 1
            x *= 2

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        res = solve(N)
        print(*res)


if __name__ == '__main__':
    main()

