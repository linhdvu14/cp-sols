''' C. Tree Infection
https://codeforces.com/contest/1665/problem/C
'''

from audioop import reverse
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

def solve(N, P):
    # get sibling group sizes
    A = {}
    for p in P: A[p] = A.get(p, 0) + 1
    A = sorted(list(A.values()), reverse=True) + [1]

    # is t injections total enough
    def is_ok(t):
        # inject group a once at time i -> infect t - i at time t
        need = 0
        for i, a in enumerate(A): need += 1 + max(a - t + i, 0)
        return need <= t

    res, lo, hi = 0, len(A), sum(A)
    while lo <= hi:
        mi = (lo + hi) // 2
        if is_ok(mi):
            res = mi
            hi = mi - 1
        else:
            lo = mi + 1

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        P = list(map(int, input().split()))
        out = solve(N, P)
        print(out)


if __name__ == '__main__':
    main()

