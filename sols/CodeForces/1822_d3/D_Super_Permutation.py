''' D. Super-Permutation
https://codeforces.com/contest/1822/problem/D
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
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

def solve(N):
    if N == 1: return [1]
    if N % 2: return [-1]
    
    A = [N] * N 
    for i in range(1, N // 2 + 1):
        if i % 2: A[i], A[-i] = i, N - i
        else: A[i], A[-i] = N - i, i

    return A


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        res = solve(N)
        print(*res)


if __name__ == '__main__':
    main()
