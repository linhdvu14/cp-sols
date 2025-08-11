''' DMOPC '22 Contest 1 P1 - Up-down Sequence
https://dmoj.ca/problem/dmopc22c1p1
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

def solve(N, A):
    sign = [0, 0]
    for i in range(1, N):
        if A[i] == 0 or A[i - 1] == 0: continue
        if A[i] == A[i - 1]: return 'NO'
        pos = 1 if A[i] > A[i - 1] else -1
        if sign[i % 2] != 0 and sign[i % 2] != pos: return 'NO'
        sign[i % 2] = pos
    
    if sign[0] != 0 and sign[0] == sign[1]: return 'NO'
    return 'YES'


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        res = solve(N, A)
        print(res)


if __name__ == '__main__':
    main()

