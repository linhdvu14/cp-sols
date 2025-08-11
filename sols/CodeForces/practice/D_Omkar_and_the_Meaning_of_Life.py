''' D. Omkar and the Meaning of Life
https://codeforces.com/contest/1583/problem/D
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

def ask(A):
    output('?', *A)
    k = int(input())
    return k - 1


def main():
    N = int(input())
    small, big = [2] * N, [1] * N

    idx = -1
    prev = [-1] * N  # prev[i] = j s.t. A[j] + 1 == A[i]

    for i in range(N):
        small[i], big[i] = 1, 2
        k, l = ask(big), ask(small)
        if k == -1: idx = i
        if k != -1 and k < i: prev[k] = i
        if l != -1 and l < i: prev[i] = l
        small[i], big[i] = 2, 1
    
    res = [-1] * N
    for v in range(N, 0, -1):
        res[idx] = v
        idx = prev[idx]

    output('!', *res)

 
if __name__ == '__main__':
    main()