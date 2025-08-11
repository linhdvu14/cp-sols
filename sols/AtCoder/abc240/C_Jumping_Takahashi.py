''' C - Jumping Takahashi
https://atcoder.jp/contests/abc240/tasks/abc240_c
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

def main():
    N, X = list(map(int, input().split()))
    S = 0
    adds = []
    for _ in range(N):
        a, b = map(int, input().split())
        X -= a
        S += b - a
        adds.append(b - a)
    if X < 0 or X > S: return False
    if X == 0 or X == S: return True

    dp = [[False]*(X+1) for _ in range(N+1)]
    for i in range(N+1): dp[i][0] = True
    
    for i, a in enumerate(adds):
        for x in range(1, X+1):
            dp[i+1][x] = dp[i][x]
            if x-a >= 0: dp[i+1][x] |= dp[i][x-a]
    return dp[-1][X]



if __name__ == '__main__':
    out = main()
    print('Yes' if out else 'No')

