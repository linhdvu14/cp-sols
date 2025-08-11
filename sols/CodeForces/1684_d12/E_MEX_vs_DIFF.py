''' E. MEX vs DIFF
https://codeforces.com/contest/1684/problem/E
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

# should transform A into {0, 1, ..., M} + {B} where M max and |B| min
# then cost is len(B)

def solve(N, K, A):
    if K >= N: return 0

    cnt = {}
    for a in A: cnt[a] = cnt.get(a, 0) + 1

    # can jump <= K times
    M = 0
    for _ in range(K):
        while M in cnt: M += 1
        M += 1
    while M in cnt: M += 1

    # by transforming <= K remaining eles, using lowest-count first
    B = [(c, a) for a, c in cnt.items() if a > M]
    B.sort()
    for i, (c, _) in enumerate(B):
        K -= c 
        if K < 0: return len(B) - i 

    return 0


def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        A = list(map(int, input().split()))
        out = solve(N, K, A)
        print(out)


if __name__ == '__main__':
    main()

