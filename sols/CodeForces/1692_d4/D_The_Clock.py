''' D. The Clock
https://codeforces.com/contest/1692/problem/D
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

def solve(s, p):
    h, m = map(int, s.split(':'))
    p = int(p)
    start = cur = h * 60 + m
    res = 0
    while True:
        cur = (cur + p) % 1440
        h, m = divmod(cur, 60)
        if h // 10 == m % 10 and h % 10 == m // 10: res += 1
        if cur == start: break
    return res


def main():
    T = int(input())
    for _ in range(T):
        s, p = input().decode().strip().split(' ')
        out = solve(s, p)
        print(out)


if __name__ == '__main__':
    main()

