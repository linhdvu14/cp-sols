''' D. Moscow Gorillas
https://codeforces.com/contest/1793/problem/D
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

def solve(N, P, Q):
    posp, posq = [-1] * (N + 1), [-1] * (N + 1)
    for i, (p, q) in enumerate(zip(P, Q)):
        posp[p] = posq[q] = i

    # mex = 1
    p, q = posp[1], posq[1]
    l, r = min(p, q), max(p, q)
    res = l * (l + 1) // 2 + (N - r - 1) * (N - r) // 2 + (r - l - 1) * (r - l) // 2

    for mex in range(2, N + 1):
        p, q = posp[mex], posq[mex]
        if not (l <= p <= r or l <= q <= r):
            nl = l + 1 
            if p < l: nl = min(nl, l - p)
            if q < l: nl = min(nl, l - q)
            nr = N - r 
            if p > r: nr = min(nr, p - r)
            if q > r: nr = min(nr, q - r)
            res += nl * nr
        l, r = min(l, p, q), max(r, p, q)

    return res + 1


def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    res = solve(N, P, Q)
    print(res)


if __name__ == '__main__':
    main()

