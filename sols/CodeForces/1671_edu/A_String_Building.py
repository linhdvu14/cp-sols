''' A. String Building
https://codeforces.com/contest/1671/problem/A
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

def solve(S):
    cnt = 0
    k = ''
    for c in S:
        if c != k:
            if cnt == 1: return 'NO'
            cnt = 0
        k = c
        cnt += 1
    if cnt == 1: return 'NO'
    return 'YES'


def main():
    T = int(input())
    for _ in range(T):
        S = input().decode().strip()
        out = solve(S)
        print(out)


if __name__ == '__main__':
    main()

