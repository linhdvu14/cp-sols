''' F - Simple Operations on Sequence
https://atcoder.jp/contests/abc232/tasks/abc232_f
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

def main():
    N, X, Y = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # swap A then increment/decrement to B
    # dp[mask] = 
    #   over all permutations PA of A whose first ln=bit_count(mask) elements PA[1..ln] are set in mask
    #   what is min cost to swap A[1..ln] to PA[1..ln], then inc/dec PA[1..ln] to B[1..ln]
    # ans is dp[(1 << N) - 1]
    dp = [INF]*(1<<N)
    dp[0] = 0

    for mask in range(1, 1<<N):
        ln = bin(mask).count('1')

        # try each prefix end: PA[ln] == A[i]
        for i in range(N):
            if not (mask >> i) & 1: continue

            # clear bit i
            # PA[1..ln] = {pmask} + A[i]
            pmask = mask & (~(1 << i))

            # min swaps required put A[i] in PA[ln] = num inversions/eles in pmask that appear after A[i] in A
            cost1 = sum(1 for j in range(i+1, N) if (pmask >> j) & 1)

            # min inc/dec PA[ln]=A[i] to B[ln] = abs(A[i] - B[ln])
            cost2 = abs(A[i] - B[ln-1])

            dp[mask] = min(dp[mask], dp[pmask] + cost1*Y + cost2*X)

    print(dp[-1])


if __name__ == '__main__':
    main()

