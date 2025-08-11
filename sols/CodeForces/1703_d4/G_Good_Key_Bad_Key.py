''' G. Good Key, Bad Key
https://codeforces.com/contest/1703/problem/G
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


from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack: return f(*args, **kwargs)
        to = f(*args, **kwargs)
        while True:
            if type(to) is GeneratorType:
                stack.append(to)
                to = next(to)
            else:
                stack.pop()
                if not stack: break
                to = stack[-1].send(to)
        return to
    return wrappedfunc


class IntKeyDict(dict):
    from random import randrange
    rand = randrange(1 << 62)
    def __setitem__(self, k, v): super().__setitem__(k^self.rand, v)
    def __getitem__(self, k): return super().__getitem__(k^self.rand)


INF = float('inf')

# -----------------------------------------

BITS = 32

def solve(N, K, A):
    # dp[i][d] = max value for A[i..] with d divisions
    # dp[i][d] = max(A[i] >> d - K + dp[i+1][d], A[i] >> (d+1) + dp[i+1][d+1])
    dp = [[0]*(BITS+1) for _ in range(N+1)]
    for i in range(N-1, -1, -1):
        for d in range(BITS-1, -1, -1):
            dp[i][d] = max((A[i] >> d) - K + dp[i+1][d], (A[i] >> (d+1)) + dp[i+1][d+1])

    return dp[0][0]


def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        A = list(map(int, input().split()))
        out = solve(N, K, A)
        print(out)


if __name__ == '__main__':
    main()

