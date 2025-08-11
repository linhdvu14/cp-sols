''' H. Sakurako's Test
https://codeforces.com/contest/2008/problem/H
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

from inspect import currentframe, getframeinfo
from re import search
DEBUG = os.environ.get('debug') not in [None, '0']

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

def solve(N, Q, A, queries):
    ps = [0] * (N + 2)
    for a in A: ps[a] += 1
    for i in range(1, N + 1): ps[i] += ps[i - 1]

    def ok(x, m):
        cnt = 0
        for k in range(N // x + 1):
            cnt += ps[min(N, k * x + m)] - ps[k * x - 1]
        return cnt > N // 2

    res = [-1] * Q
    memo = {}
    for i, x in enumerate(queries):
        if x not in memo:
            med, lo, hi = -1, 0, x - 1
            while lo <= hi:
                mi = (lo + hi) // 2
                if ok(x, mi):
                    med = mi
                    hi = mi - 1
                else:
                    lo = mi + 1
            memo[x] = med 
        res[i] = memo[x]

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, Q = list(map(int, input().split()))
        A = list(map(int, input().split()))
        queries = [int(input()) for _ in range(Q)]
        res = solve(N, Q, A, queries)
        print(*res)


if __name__ == '__main__':
    main()

