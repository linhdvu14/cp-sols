''' A. Subtle Substring Subtraction
https://codeforces.com/contest/1673/problem/0
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
    S = [ord(c) - ord('a') + 1 for c in S]
    a, b = sum(S), 0
    if len(S) % 2 == 1:
        b = min(S[0], S[-1])
        a -= b
    res = 'Alice' if a > b else 'Bob'
    return res, abs(a - b)


def main():
    T = int(input())
    for _ in range(T):
        S = input().decode().strip()
        out = solve(S)
        print(*out)


if __name__ == '__main__':
    main()

