''' Problem C2: Back in Black (Chapter 2)
https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-1/problems/C2
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

def solve():
    N = int(input())
    S = [-1] + list(map(int, list(input().strip())))
    
    cnt = 0
    for i in range(1, N + 1):
        if not S[i]: continue
        cnt += 1
        for j in range(i + i, N + 1, i):
            S[j] ^= 1

    res = 0
    Q = int(input())
    for _ in range(Q):
        i = int(input())
        if S[i]: cnt -= 1
        else: cnt += 1
        S[i] ^= 1
        res += cnt

    return res


def main():
    T = int(input())
    for t in range(T):
        res = solve()
        print(f'Case #{t + 1}: {res}')



if __name__ == '__main__':
    main()
