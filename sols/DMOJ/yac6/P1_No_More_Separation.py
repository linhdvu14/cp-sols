''' Yet Another Contest 6 P1 - No More Separation
https://dmoj.ca/problem/yac6p1
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
    rem = M 
    for i in range(N):
        if not rem: break 
        for j in range(i + 1, N):
            print(i + 1, j + 1)
            rem -= 1
            if not rem: break


if __name__ == '__main__':
    main()

