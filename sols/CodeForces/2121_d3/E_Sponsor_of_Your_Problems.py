''' E. Sponsor of Your Problems
https://codeforces.com/contest/2121/problem/E 
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

def solve(L, R):
    N = len(L)
    
    res = i = 0
    while i < N and L[i] == R[i]:
        res += 2
        i += 1
    
    if i < N and int(R[i]) - int(L[i]) == 1:
        res += 1
        i += 1
        while i < N and L[i] == '9' and R[i] == '0':
            res += 1
            i += 1
    
    return res


def main():
    T = int(input())
    for _ in range(T):
        L, R = input().decode().strip().split()
        res = solve(L, R)
        print(res)


if __name__ == '__main__':
    main()

