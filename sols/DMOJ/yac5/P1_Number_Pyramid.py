''' Yet Another Contest 5 P1 - Number Pyramid
https://dmoj.ca/problem/yac5p1
'''

import os, sys
input = sys.stdin.readline  # strip() if str

def debug(*args):   
    if os.environ.get('debug') in [None, '0']: return
    from inspect import currentframe, getframeinfo
    from re import search
    frame = currentframe().f_back
    s = getframeinfo(frame).code_context[0]
    r = search(r"\((.*)\)", s).group(1)
    vnames = r.split(', ')
    var_and_vals = [f'{var}={val}' for var, val in zip(vnames, args)]
    prefix = f'{currentframe().f_back.f_lineno:02d}: '
    print(f'{prefix}{", ".join(var_and_vals)}')

INF = float('inf')

# -----------------------------------------


# x, x, x, .... x, y         --> N 
# 2x, 2x, 2x, ..., 2x, x + y --> N - 1
# 4x, 4x, 4x, ...., 4x, 3x + y --> N - 2
# 2^i x, ...., 2^i x, 2^i x + y - x --> N - i
# (2^(N - 1) - 1) * x + y --> 1

def solve(N, K, X):
    x = K - 1
    y = (X - (pow(2, N - 1, K) - 1) * x) % K
    return [x] * (N - 1) + [y]



def main():
    N, K, X = list(map(int, input().split()))
    res = solve(N, K, X)
    print(*res)


if __name__ == '__main__':
    main()

