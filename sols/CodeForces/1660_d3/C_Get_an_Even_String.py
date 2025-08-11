''' C. Get an Even String
https://codeforces.com/contest/1660/problem/C
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

def solve_1(S):
    N = len(S)

    # dp[i] = min cost to make S[..i] valid
    dp = [0] * (N+1)
    prev = [-1] * 26

    for i, c in enumerate(S):
        c = ord(c) - ord('a')
        if prev[c] == -1:
            dp[i+1] = dp[i] + 1
        else:
            dp[i+1] = min(dp[i] + 1, i - prev[c] - 1 + dp[prev[c]])
        prev[c] = i

    return dp[-1]


# greedily partition S into max nums of non-overlapping intervals with start == end
def solve_2(S):
    N = len(S)
    cnt = i = 0
    while i < N:
        seen = set()
        for j in range(i, N):
            if S[j] in seen: 
                cnt += 1
                break
            seen.add(S[j])
        i = j + 1
    return N - cnt*2


solve = solve_2

def main():
    T = int(input())
    for _ in range(T):
        S = input().decode().strip()
        out = solve(S)
        print(out)


if __name__ == '__main__':
    main()
 