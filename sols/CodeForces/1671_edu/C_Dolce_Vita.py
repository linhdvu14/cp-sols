''' C. Dolce Vita
https://codeforces.com/contest/1671/problem/C
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

def solve(N, X, A):
    A.sort()
    P = [0]
    for a in A: P.append(P[-1] + a)

    # num days can buy from the cheapest n shops
    res = t = 0
    for n in range(N, 0, -1):
        nxt_t = (X - P[n]) // n
        if nxt_t < t: continue
        res += n * (nxt_t - t + 1)
        t = nxt_t + 1

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, X = list(map(int, input().split()))
        A = list(map(int, input().split()))
        out = solve(N, X, A)
        print(out)


if __name__ == '__main__':
    main()

