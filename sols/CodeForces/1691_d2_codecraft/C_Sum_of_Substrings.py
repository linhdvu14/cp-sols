''' C. Sum of Substrings
https://codeforces.com/contest/1691/problem/C
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

# each 1 contributes 11, except S[0] contributes 10 and S[-1] contributes 1

def solve(N, K, S):
    # last pos should be 1
    if S[-1] == 0:
        for i in range(N-2, -1, -1):
            if S[i] == 1 and (N - 1 - i) <= K:
                K -= N - 1 - i 
                S[i], S[-1] = S[-1], S[i]
                break
    
    # first pos should be 1
    if S[0] == 0:
        for i in range(1, N-1):
            if S[i] == 1 and i <= K:
                K -= i
                S[i], S[0] = S[0], S[i]
                break

    res = 0
    for i, c in enumerate(S):
        if i > 0: res += c
        if i < N-1: res += 10 * c

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        S = list(map(int, list(input().decode().strip())))
        out = solve(N, K, S)
        print(out)


if __name__ == '__main__':
    main()

