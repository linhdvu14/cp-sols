''' B. Make AP
https://codeforces.com/contest/1624/problem/B
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

def solve(a, b, c):
    a2 = c - (c - b) * 2
    if a2 > 0 and a2 % a == 0: return True

    b2 = (a + c) // 2
    if b2 > 0 and b2 % b == 0 and 2*b2 == a + c: return True

    c2 = a + 2 * (b - a)
    if c2 > 0 and c2 % c == 0: return True
    
    return False


def main():
    T = int(input())
    for _ in range(T):
        a, b, c = list(map(int, input().split()))
        out = solve(a, b, c)
        print('YES' if out else 'NO')


if __name__ == '__main__':
    main()

