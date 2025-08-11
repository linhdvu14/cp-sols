''' D. For Gamers. By Gamers.
https://codeforces.com/contest/1657/problem/D
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

# for good (d, h, c), need to purchase min t s.t. dht > DH
# cost is ct
def solve(N, M, C, goods, enemies):
    # c -> max(d*h)
    choices = [0] * (C+1)
    for c, d, h in goods:
        choices[c] = max(choices[c], d*h)

    # power[ct] = max(dht) over all goods
    power = [0] * (C+1)
    for c, dh in enumerate(choices):
        if dh == 0: continue
        t = 1
        while t*c <= C:
            power[t*c] = max(power[t*c], t*dh)
            t += 1
    
    for i in range(1, C+1):
        power[i] = max(power[i], power[i-1])
    
    # find min ct s.t. dht > DH
    res = [-1] * M
    for i, (D, H) in enumerate(enemies):
        cost, lo, hi = -1, 0, C
        D *= H
        while lo <= hi:
            mi = (lo + hi) // 2
            if power[mi] > D:
                cost = mi
                hi = mi - 1
            else:
                lo = mi + 1
        if cost != -1: res[i] = cost

    return res


def main():
    N, C = list(map(int, input().split()))
    goods = [list(map(int, input().split())) for _ in range(N)]
    M = int(input())
    enemies = [list(map(int, input().split())) for _ in range(M)]
    out = solve(N, M, C, goods, enemies)
    print(*out)


if __name__ == '__main__':
    main()

