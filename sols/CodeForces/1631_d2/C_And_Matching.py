''' C. And Matching
https://codeforces.com/contest/1631/problem/C
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') not in [None, '0']

if DEBUG:
    from inspect import currentframe, getframeinfo
    from re import search

def debug(*args):
    if not DEBUG: return
    frame = currentframe().f_back
    s = getframeinfo(frame).code_context[0]
    r = search(r"\((.*)\)", s).group(1)
    vnames = r.split(', ')
    var_and_vals = [f'{var}={val}' for var, val in zip(vnames, args)]
    prefix = f'{currentframe().f_back.f_lineno:02d}: '
    print(f'{prefix}{", ".join(var_and_vals)}')


INF = float('inf')

# -----------------------------------------

def solve(N, K):
    if K == 0:  # pair each num with its flip
        for i in range(N//2):
            print(i, N-1-i)
    elif K == N-1:
        if N == 4:
            print(-1)
        else:
            print(N-2, N-1)
            print(1, 3)
            print(0, N-4)
            for i in range(2, N//2):
                if i != 3:
                    print(i, N-1-i)
    else:
        print(K, N-1)
        print(N-1-K, 0)
        for i in range(1, N//2):
            if i != K and i != N-1-K:
                print(i, N-1-i)


def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        solve(N, K)


if __name__ == '__main__':
    main()

