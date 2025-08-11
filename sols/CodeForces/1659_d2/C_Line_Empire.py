''' C. Line Empire
https://codeforces.com/contest/1659/problem/C
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

def solve(N, a, b, X):
    # pref[i] = dist(0, X[0]) + dist(0, X[1]) + ... + dist(0, X[i-1])
    pref = [0]
    for x in X: pref.append(pref[-1] + x)

    # until last capital, can pay 1 unit of moving cost in advance with every conquer
    # -> 1 op = conquer next pos + move to next pos
    res = pref[N] * b
    cur = px = 0

    # try last capital at x
    for i, x in enumerate(X): 
        cur += (x - px) * (a + b)
        cand = cur + (pref[N] - pref[i] - x * (N - i)) * b
        res = min(res, cand)
        px = x

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, a, b = list(map(int, input().split())) 
        X = list(map(int, input().split()))
        out = solve(N, a, b, X)
        print(out)


if __name__ == '__main__':
    main()

