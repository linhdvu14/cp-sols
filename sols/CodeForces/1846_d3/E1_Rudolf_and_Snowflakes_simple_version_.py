''' E1. Rudolf and Snowflakes (simple version)
https://codeforces.com/contest/1846/problem/E1
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

MAX = 10**6
MAX_K = 100

# 1 + k + k^2 + ...
GOOD = set()
for k in range(2, MAX_K + 1):
    s = 1 + k + k * k
    km = k * k
    while s <= MAX:
        GOOD.add(s)
        km *= k 
        s += km 

def solve(n):
    # (1 - k^x) / (1 - k)
    if n in GOOD: return 'YES'

    # n = 1 + k + k^2
    sq = max(int((n - 1)**0.5), 2)
    for k in range(sq, sq + 2):
        if 1 + k + k * k == n:
            return 'YES'

    return 'NO'


def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        res = solve(n)
        print(res)


if __name__ == '__main__':
    main()
