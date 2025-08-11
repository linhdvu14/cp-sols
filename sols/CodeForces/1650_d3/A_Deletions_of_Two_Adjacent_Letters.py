''' A. Deletions of Two Adjacent Letters
https://codeforces.com/contest/1650/problem/A
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

def solve(S, c):
    for i, a in enumerate(S):
        if a == c and i % 2 == 0:
            return True
    return False


def main():
    T = int(input())
    for _ in range(T):
        S = input().decode().strip()
        c = input().decode().strip()
        out = solve(S, c)
        print('YES' if out else 'NO')


if __name__ == '__main__':
    main()

