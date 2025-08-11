''' D1. 388535 (Easy Version)
https://codeforces.com/contest/1658/problem/D1
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

# if at any bit pos, cnt 0 == cnt 1
# then must have even num eles with same prefix since L = 0
# so ok to set corresponding bit of X to either 0 or 1

def solve(L, R, A):
    if (R - L + 1) % 2 == 1:
        res = 0
        for i, a in enumerate(A):
            res ^= a
            res ^= i
        return res

    cnt_i = [0] * 18
    cnt_a = [0] * 18
    for i, a in enumerate(A):
        for b in range(18):
            if (i >> b) & 1 == 1: cnt_i[b] += 1
            if (a >> b) & 1 == 1: cnt_a[b] += 1

    res = 0
    for b in range(18):
        res <<= 1
        if cnt_i[17-b] != cnt_a[17-b]:
            res |= 1
    return res


def main():
    T = int(input())
    for _ in range(T):
        L, R = list(map(int, input().split()))
        A = list(map(int, input().split()))
        out = solve(L, R, A)
        print(out)


if __name__ == '__main__':
    main()

