''' D. Palindromes Coloring
https://codeforces.com/contest/1624/problem/D
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

def solve(N, K, S):
    cnt = [0]*26
    for c in S: cnt[ord(c) - ord('a')] += 1
    
    pairs = sum(c // 2 for c in cnt)
    free = pairs % K * 2 + sum(c % 2 for c in cnt)
    base = pairs // K * 2 + (free >= K)

    return base


def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        S = input().decode().strip()
        out = solve(N, K, S)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

