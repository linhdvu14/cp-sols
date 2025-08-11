''' A. Forbidden Integer
https://codeforces.com/contest/1845/problem/A
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

def solve(N, K, X):
    if X != 1: return 'YES', [1] * N
    if K == 1: return 'NO', []
    if N % 2 == 0: return 'YES', [2] * (N // 2)
    if K == 2: return 'NO', []
    return 'YES', [2] * (N // 2 - 1) + [3]


def main():
    T = int(input())
    for _ in range(T):
        N, K, X = list(map(int, input().split()))
        a, b = solve(N, K, X)
        print(a)
        if b: 
            print(len(b))
            print(*b)


if __name__ == '__main__':
    main()

