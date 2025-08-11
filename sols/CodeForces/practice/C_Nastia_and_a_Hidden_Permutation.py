''' C. Nastia and a Hidden Permutation
https://codeforces.com/contest/1521/problem/C
'''

import functools
import os, sys
input = sys.stdin.readline  # strip() if str; io.BytesIO(os.read(0,os.fstat(0).st_size)).readline doesn't work
output = functools.partial(print, flush=True)

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

def ask(t, x, i, j):
    output(f'? {t} {i + 1} {j + 1} {x}')
    res = int(input())
    assert res != -1
    return res

def find(i, N):
    for j in range(N):
        if j != i: return j


# let f(t, x, a, b) 
# f(1, N - 1, a, b) = max(min(N - 1, a), b) 
#   * = N - 1 if a == N else max(a, b) 
#   * = N iff b == N
# f(2, 1, a, b) = min(a, max(2, b)) 
#   * = 2 if b == 1 else min(a, b)
#   * = 1 iff a == 1
# f(1, N - 1, 1, b) = b

def solve():
    N = int(input())

    # find idx of 1
    idx = N - 1
    for i in range(0, N - 1, 2):
        mn = ask(2, 1, i, i + 1)
        if mn == 1: idx = i
        elif mn == 2 and ask(2, 1, i + 1, find(i + 1, N)) == 1: idx = i + 1
        if idx != N - 1: break

    # fill in rest
    res = [-1] * N
    for i in range(N):
        if i == idx: res[i] = 1
        else: res[i] = ask(1, N - 1, idx, i)

    output('!', *res)


def main():
    T = int(input())
    for _ in range(T):
        solve()

 
if __name__ == '__main__':
    main()