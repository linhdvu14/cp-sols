''' C. Menorah
https://codeforces.com/contest/1615/problem/C
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') is not None

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

def solve(N, A, B):
    cnt00 = cnt01 = cnt10 = cnt11 = 0
    for a, b in zip(A, B):
        if a=='1' and b=='1': cnt11 += 1
        if a=='1' and b=='0': cnt10 += 1
        if a=='0' and b=='1': cnt01 += 1
        if a=='0' and b=='0': cnt00 += 1

    res = INF

    # even total, all diff flip once
    # note 2 ops = swap a 0 and 1
    if cnt01 == cnt10: res = min(res, cnt01 + cnt10)

    # odd total, all same flip once
    if cnt11 == cnt00 + 1: res = min(res, cnt00 + cnt11)

    return res if res < INF else -1


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = input().decode().strip()
        B = input().decode().strip()
        out = solve(N, A, B)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

