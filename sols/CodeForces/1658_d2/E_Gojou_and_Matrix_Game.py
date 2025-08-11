''' E. Gojou and Matrix Game
https://codeforces.com/contest/1658/problem/E
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

# take turns placing token on cell with value > value of previous cell
# last player wins

def main():
    N, K = list(map(int, input().split()))

    # dp[r][c] = does placing token on (r, c) win
    dp = [['G'] * N for _ in range(N)]

    # dp[r][c] = 1 iff all (r', c') where V[r'][c'] > V[r][c] and dp[r'][c'] == 1 have dist(r, c, r', c') <= K
    # |r-r'] + |c-c'| = max(|(r+c) - (r'+c')|, |(r-c) - (r'-c')|) <= K
    idx = [None] * N * N
    for r in range(N):
        row = map(int, input().split())
        for c, v in enumerate(row):
            idx[v-1] = (r, c)

    mns, mxs, mnd, mxd = INF, -INF, INF, -INF
    for r, c in idx[::-1]:
        s, d = r + c, r - c
        if mns is INF or max(abs(s - mxs), abs(s - mns), abs(d - mxd), abs(d - mnd)) <= K:
            dp[r][c] = 'M'
            mns, mxs = min(mns, s), max(mxs, s)
            mnd, mxd = min(mnd, d), max(mxd, d)
    
    for r in range(N): print(''.join(dp[r]))


if __name__ == '__main__':
    main()

