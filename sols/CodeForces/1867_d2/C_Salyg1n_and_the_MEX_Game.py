''' C. Salyg1n and the MEX Game
https://codeforces.com/contest/1867/problem/C
'''

import os, sys
input = sys.stdin.buffer.readline
output = lambda x: os.write(1, str(x).encode('ascii') + b'\n')

DEBUG = os.environ.get('debug') not in [None, '0']

def debug(*args):   
    if not DEBUG: return
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

def move(x):
    output(x)
    y = int(input())
    assert y != -2
    return y


def solve(N, A):
    i = 0
    while i < N and A[i] == i: i += 1
    while i >= 0: i = move(i)


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        solve(N, A)
    

if __name__ == '__main__':
    main()

