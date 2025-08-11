''' E. Masha-forgetful
https://codeforces.com/contest/1624/problem/E
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') is not None

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

def solve(N, M, strs, S):
    # rmb bigrams and trigrams
    known = {}
    for si, s in enumerate(strs):
        for i in range(M):
            if i+2 <= M: known[s[i:i+2]] = (i+1, i+2, si+1)
            if i+3 <= M: known[s[i:i+3]] = (i+1, i+3, si+1)

    # dp[i] = S[i:] is good
    dp = [False]*M + [True]
    for i in range(M-1, -1, -1):
        if i+2 <= M and S[i:i+2] in known and dp[i+2]: dp[i] = True
        if i+3 <= M and S[i:i+3] in known and dp[i+3]: dp[i] = True

    if not dp[0]: return -1, []

    res = []
    i = 0
    while i < M:
        if i+2 <= M and dp[i+2]: 
            res.append(known[S[i:i+2]])
            i += 2
        else:
            res.append(known[S[i:i+3]])
            i += 3

    return len(res), res




def main():
    T = int(input())
    for _ in range(T):
        _ = input()
        N, M = list(map(int, input().split()))
        strs = [input().decode().strip() for _ in range(N)]
        S = input().decode().strip()
        r1, r2 = solve(N, M, strs, S)
        print(r1)
        for seq in r2: print(*seq)


if __name__ == '__main__':
    main()

