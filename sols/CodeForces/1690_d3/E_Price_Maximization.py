''' E. Price Maximization
https://codeforces.com/contest/1690/problem/E
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

from collections import deque

def solve(N, K, A):
    res = 0
    for i, a in enumerate(A):
        res += a // K
        A[i] = a % K
    
    # each pairing add at most 1 gain (if sum >= K)
    # should pair a with min b s.t. a + b >= K; or next_greater(a) if no such b
    # alternatively best to pair max with min if sum >= K, else rm 2 mins 
    A = deque(sorted(A))
    while A:
        if A[0] + A[-1] >= K:
            res += 1
            A.popleft()
            A.pop()
        else:
            A.popleft()
            A.popleft()

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        A = list(map(int, input().split()))
        out = solve(N, K, A)
        print(out)


if __name__ == '__main__':
    main()

