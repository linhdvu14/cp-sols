''' G. Gangsta
https://codeforces.com/contest/2121/problem/G
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

from inspect import currentframe, getframeinfo
from re import search
DEBUG = os.environ.get('debug') not in [None, '0']

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
# (c1 + c0) + abs(c1 - c0)
def solve(N, S):
    bals = [0] * (N + 1)
    for i, c in enumerate(S):
        bals[i + 1] = bals[i] + (1 if c == '1' else -1)
    bals.sort()

    res = ln = 0
    for i in range(N):
        ln += i + 1
        res += ln
    
    for i, b in enumerate(bals):
        res += b * i - b * (N - i)

    return res // 2



def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = input().decode().strip()
        res = solve(N, S)
        print(res)


if __name__ == '__main__':
    main()

