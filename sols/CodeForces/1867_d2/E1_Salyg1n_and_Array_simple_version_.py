''' E1. Salyg1n and Array (simple version)
https://codeforces.com/contest/1867/problem/E1
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

def ask(x):
    output(f'? {x}')
    res = int(input())
    assert res != -1
    return res


def answer(x):
    output(f'! {x}')


def solve(N, K):
    x = 0
    for i in range(0, N - K + 1, K): x ^= ask(i + 1)
    for i in range(N % K): x ^= ask(N - N % K - K + 2 + i)
    answer(x)


def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        solve(N, K)


if __name__ == '__main__':
    main()

