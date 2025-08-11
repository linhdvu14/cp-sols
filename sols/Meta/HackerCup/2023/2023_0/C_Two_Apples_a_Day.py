''' Problem C: Two Apples a Day
https://www.facebook.com/codingcompetitions/hacker-cup/2023/practice-round/problems/C
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

def solve(N, A):
    if N == 1: return 1

    N = 2 * N - 1
    A.sort()

    # leftmost: * | 0 1 2 3 4
    s = A[0] + A[-2]
    cand = s - A[-1]
    if cand > 0 and all(A[i] + A[N - 2 - i] == s for i in range(1, N // 2)): return cand
    
    # mid
    s = A[0] + A[-1]
    cand = -1
    l, r = 1, N - 2
    while l <= r:
        s2 = A[l] + A[r]
        if s2 != s and cand != -1: break
        if s2 < s:  # satisfy l
            cand = s - A[l]
            l += 1
        elif s2 > s or l == r:
            cand = s - A[r]
            r -= 1
        else:
            l += 1
            r -= 1
    else:
        if cand > 0: return cand 

    # right: 0 1 2 3 4 | *
    s = A[1] + A[-1]
    cand = s - A[0]
    if cand > 0 and all(A[i] + A[-i] == s for i in range(2, N // 2 + 1)): return cand
    
    return -1


def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        res = solve(N, A)
        print(f'Case #{t + 1}: {res}')


if __name__ == '__main__':
    main()

