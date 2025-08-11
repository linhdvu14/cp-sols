''' D. Cheater
https://codeforces.com/contest/2113/problem/D
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

def solve(N, A, B):
    suff_mx = [0] * (N + 1)
    for i in range(N):
        suff_mx[i + 1] = max(suff_mx[i], A[-i - 1])
    
    pref_mns = [[INF, INF] for _ in range(N + 1)]
    cur = [INF, INF]
    for i, a in enumerate(A):
        cur = sorted(cur + [a])[:2]
        pref_mns[i + 1] = cur[:]

    def ok(nb):
        b = min(B[:nb + 1])
        a = sorted(pref_mns[N - nb] + [suff_mx[nb]])[1]
        return a > b

    res, lo, hi = N, 0, N 
    while lo <= hi:
        mi = (lo + hi) // 2
        if ok(mi):
            res = mi
            hi = mi - 1
        else:
            lo = mi + 1
    
    return N - res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        res = solve(N, A, B)
        print(res)


if __name__ == '__main__':
    main()

