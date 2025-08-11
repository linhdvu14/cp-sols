''' Problem A: Here Comes Santa Claus
https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-1/problems/A
'''

import os, sys
input = sys.stdin.readline  # strip() if str
output = sys.stdout.write

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
    A.sort()
    if N == 5: return max(A[4] + A[2] - A[0] - A[1], A[4] + A[3] - A[0] - A[2]) / 2
    return (A[-1] + A[-2] - A[0] - A[1]) / 2



def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        res = solve(N, A)
        print(f'Case #{t + 1}: {res}')


if __name__ == '__main__':
    main()

