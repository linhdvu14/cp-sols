''' B. Palindromic Numbers
https://codeforces.com/contest/1700/problem/B
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

# for int dict key
from random import randrange
RAND = randrange(1 << 62)
def conv(x): return x ^ RAND

INF = float('inf')

# -----------------------------------------

def solve(N, S):
    # 9..9
    res = [9 - int(c) for c in S]
    if res[0] != 0: return res

    # 110..011; add 12
    res[0] = 1
    for _ in range(12):
        carry = 1
        for i in range(N-1, -1, -1):
            carry, res[i] = divmod(res[i] + carry, 10)
            if not carry: break
    
    return res



def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = input().decode().strip()
        out = solve(N, S)
        print(*out, sep='')


if __name__ == '__main__':
    main()

