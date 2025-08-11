''' C. Tokitsukaze and Strange Inequality
https://codeforces.com/contest/1678/problem/C
'''

import io, os, sys
input = sys.stdin.readline
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

def solve(N, P):
    # pref[i][j] = num eles in 0..j-1 < P[i]
    pref = [[0]*(N+1) for _ in range(N)]
    for i in range(N):
        cnt = 0
        for j in range(N):
            if P[j] < P[i]: cnt += 1
            pref[i][j+1] = cnt

    res = 0
    for c in range(N-1):
        for b in range(1, c):
            a = pref[c][b]
            d = pref[b][N] - pref[b][c+1]
            res += a * d
    return res



def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        P = list(map(int, input().split()))
        out = solve(N, P)
        print(out)


if __name__ == '__main__':
    main()

