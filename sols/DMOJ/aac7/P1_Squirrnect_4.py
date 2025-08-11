''' An Animal Contest 7 P1 - Squirrnect 4
https://dmoj.ca/problem/aac7p1
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

def solve(R, C):
    if C == 1: return 'bad'
    if R < 4 and C < 4: return 'bad'
    if R == 1 and C < 7: return 'bad'
    return 'good'


def main():
    T = int(input())
    for _ in range(T):
        C, R = list(map(int, input().split()))
        res = solve(R, C)
        print(res)


if __name__ == '__main__':
    main()

