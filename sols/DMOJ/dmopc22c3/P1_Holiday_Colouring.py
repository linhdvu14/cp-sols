''' DMOPC '22 Contest 3 P1 - Holiday Colouring
https://dmoj.ca/problem/dmopc22c3p1
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

def main():
    N, M = list(map(int, input().split()))
    if N * M % 2 == 0:  # G mirrors R
        r = g = N * M // 2   
    else:   # R starts at center
        r = min((N + 1) // 2 * M, (M + 1) // 2 * N)
        g = N * M - r
    print(r, g)


if __name__ == '__main__':
    main()

