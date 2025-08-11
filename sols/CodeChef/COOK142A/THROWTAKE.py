''' Throw and Take
https://www.codechef.com/COOK142A/problems/THROWTAKE
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

# f(i, p) = max score if current player starts at pile i and pile i has parity p remaining coins
# f(i, 0) = s
# f(i, 1) = max(s, V[i] - s)
# where s = max(0, V[j] - f(j, (C[j] - 1) & 1)) for i < j < N

def solve(N, C, V):
    dp = [[0] * 2 for _ in range(N)]
    dp[N-1][1] = V[N-1]
    s = max(0, V[N-1] - dp[N-1][(C[N-1] - 1) & 1])
    for i in range(N-2, -1, -1):
        dp[i][0] = s
        dp[i][1] = max(s, V[i] - s)
        s = max(s, V[i] - dp[i][(C[i] - 1) & 1])
    return dp[0][C[0] & 1]



def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        C = list(map(int, input().split()))
        V = list(map(int, input().split()))
        out = solve(N, C, V)
        print(out)


if __name__ == '__main__':
    main()

