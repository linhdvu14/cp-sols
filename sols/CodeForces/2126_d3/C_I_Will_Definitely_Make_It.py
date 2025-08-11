''' C. I Will Definitely Make It
https://codeforces.com/contest/2126/problem/C
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

def solve(N, K, H):
    start = H[K - 1]
    H = sorted(list(set(h for h in H if h >= start)))
    
    lv = 1
    for i in range(1, len(H)):
        lv += H[i] - H[i - 1]
        if lv - 1 > H[i - 1]: return 'NO'

    return 'YES'


def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        H = list(map(int, input().split()))
        res = solve(N, K, H)
        print(res)


if __name__ == '__main__':
    main()

