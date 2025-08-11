''' A. ABC
https://codeforces.com/contest/1632/problem/A
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

def solve(N, S):
    c0 = S.count('0')
    c1 = S.count('1')
    return N == 1 or c0 == c1 == 1


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = input().decode().strip()
        out = solve(N, S)
        print('YES' if out else 'NO')


if __name__ == '__main__':
    main()

