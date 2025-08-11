''' C. Minimize Distance
https://codeforces.com/contest/1591/problem/C
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') is not None

if DEBUG:
    from varname.core import argname
    from inspect import currentframe

def debug(var, *more_vars):
    if not DEBUG: return
    var_names = argname('var', '*more_vars', func=debug)
    values = (var, *more_vars)
    name_and_values = [f'{var_name}={value}'  for var_name, value in zip(var_names, values)]
    prefix = f'{currentframe().f_back.f_lineno:02d}: '
    print(f'{prefix}{", ".join(name_and_values)}')


INF = float('inf')

# -----------------------------------------

from heapq import heappush, heappop

def solve1(N, K, A):
    L = [-a for a in A if a < 0]
    R = [a for a in A if a > 0]
    if not L and not R: return 0
    L.sort()
    R.sort()
    
    def solve(A, k):
        if not A: return 0
        N = len(A)

        # dp[i] = min cost to deliver to A[0]..A[i] and return to 0
        dp = [INF]*N
        heap = []
        for i in range(min(K, N)):
            dp[i] = 2*A[i]
            heappush(heap, (dp[i], i))

        for i in range(K, N):
            mn = idx = -1
            while idx < i-k:
                mn, idx = heappop(heap)
            dp[i] = mn + 2*A[i]
            heappush(heap, (dp[i], i))

        return dp[-1]
    
    res = solve(L, K) + solve(R, K)
    if not L: return res - R[-1]
    if not R: return res - L[-1]
    return res - max(R[-1], L[-1])


# cost to deliver i..j is 2*j
# from farthest point inward, should deliver as much as possible 
def solve2(N, K, A):    
    L = [-a for a in A if a < 0] + [0]
    R = [a for a in A if a > 0] + [0]
    L.sort(reverse=True)
    R.sort(reverse=True)
    res = -max(L[0], R[0])
    for i in range(0, len(L), K):
        res += 2*L[i]
    for i in range(0, len(R), K):
        res += 2*R[i]
    return res


solve = solve2

def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        A = list(map(int, input().split()))
        out = solve(N, K, A)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

