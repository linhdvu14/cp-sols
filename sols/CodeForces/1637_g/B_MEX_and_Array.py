''' B. MEX and Array
https://codeforces.com/contest/1637/problem/B
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

# given array A, how to partition to max value ?
# initially put each ele in its own partition
# should only join 2 partitions (a, b) if a=0 and b=1 (or vice versa)
# then num partitions decreases by 1 and sum mex({a, b}) increases by 1
# so should just put each ele in its own partition

def solve(N, A):
    res = 0
    for i in range(N):
        for j in range(i, N):
            zero = 0
            for k in range(i, j+1):
                if A[k] == 0:
                    zero += 1
            res += zero + j - i + 1
    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        out = solve(N, A)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

