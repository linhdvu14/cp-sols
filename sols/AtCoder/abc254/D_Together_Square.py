''' D - Together Square
https://atcoder.jp/contests/abc254/tasks/abc254_d
'''

import io, os, sys
from re import X
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

def solve(N):
    lpf = [0] * (N+1)
    primes = []
    for i in range(2, N+1):
        if lpf[i] == 0:
            lpf[i] = i
            primes.append(i)
        for p in primes:
            if p*i > N or p > lpf[i]: break 
            lpf[p*i] = p 
    
    # let x = x0 * (x1^2), y = y0 * (y1^2)
    # xy is square iff x0 == y0
    cnt = {}
    for a in range(1, N+1):
        c = {}
        while a > 1:
            c[lpf[a]] = c.get(lpf[a], 0) + 1
            a //= lpf[a]
        x = 1
        for k, v in c.items():
            if v % 2 == 1:
                x *= k
        cnt[x] = cnt.get(x, 0) + 1
    
    return sum(v * (v-1) for v in cnt.values()) + N


def main():
    N = int(input())
    out = solve(N)
    print(out)


if __name__ == '__main__':
    main()
