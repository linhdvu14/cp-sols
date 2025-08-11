''' Problem C1: Back in Black (Chapter 1)
https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-1/problems/C1
'''

import os, sys
input = sys.stdin.readline  # strip() if str
output = sys.stdout.write

def debug(*args):   
    if os.environ.get('debug') in [None, '0']: return
    from inspect import currentframe, getframeinfo
    from re import search
    frame = currentframe().f_back
    s = getframeinfo(frame).code_context[0]
    r = search(r"\((.*)\)", s).group(1)
    vnames = r.split(', ')
    var_and_vals = [f'{var}={val}' for var, val in zip(vnames, args)]
    prefix = f'{currentframe().f_back.f_lineno:02d}: '
    print(f'{prefix}{", ".join(var_and_vals)}')

INF = float('inf')

# -----------------------------------------
from collections import defaultdict

def solve():
    N = int(input())
    S = list(map(int, list(input().strip())))

    Q = int(input())
    queries = defaultdict(int)
    for _ in range(Q):
        x = int(input())
        queries[x] ^= 1

    for x, c in queries.items():
        if not c: continue
        for i in range(x - 1, N, x):
            S[i] ^= 1
    
    res = 0
    for i in range(N):
        if not S[i]: continue
        res += 1
        for j in range(i, N, i + 1):
            S[j] ^= 1

    return res


def main():
    T = int(input())
    for t in range(T):
        res = solve()
        print(f'Case #{t + 1}: {res}')



if __name__ == '__main__':
    main()
