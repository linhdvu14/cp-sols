''' B. Promo
https://codeforces.com/contest/1697/problem/B
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


def main():
    N, Q = list(map(int, input().split()))
    P = list(map(int, input().split()))
    P.sort()

    pref = [0]
    for p in P: pref.append(pref[-1] + p)

    res = []
    for _ in range(Q):
        x, y = list(map(int, input().split()))
        v = pref[N - x + y] - pref[N - x]
        res.append(v)

    print(*res, sep='\n')



if __name__ == '__main__':
    main()

