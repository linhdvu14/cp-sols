''' G. Hits Different
https://codeforces.com/contest/1829/problem/G
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
from bisect import bisect_right
MAX = 10**6

START, PS = [], []
i = ln = 1
while i < MAX:
    ps = [0] * (ln + 1)
    for d in range(ln): ps[d] = ps[d - 1] + (i + d) * (i + d)
    START.append(i)
    PS.append(ps)
    i += ln 
    ln += 1


def solve(n):
    res = 0
    row = bisect_right(START, n) - 1
    l = r = n - START[row]
    for i in range(row, 0, -1):
        res += PS[i][r] - PS[i][l - 1]
        l = max(0, l - 1)
        r = min(r, i - 1)

    return res + 1


def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        res = solve(n)
        print(res)


if __name__ == '__main__':
    main()

