''' C. Monsters And Spells
https://codeforces.com/contest/1626/problem/C
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug')

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

def solve(N, K, H):
    intervals = []
    for k, h in zip(K, H):
        intervals.append((k-h+1, k))
    intervals.sort()

    res = 0
    l, r = intervals[0]
    for i in range(1, len(intervals)):
        l2, r2 = intervals[i]
        if l2 > r:
            h = r - l + 1
            res += h * (h+1) // 2
            l, r = l2, r2
        else:
            r = max(r, r2)

    h = r - l + 1
    res += h * (h+1) // 2

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        K = list(map(int, input().split()))
        H = list(map(int, input().split()))
        out = solve(N, K, H)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

