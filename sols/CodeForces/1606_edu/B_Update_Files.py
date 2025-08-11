''' B. Update Files
https://codeforces.com/contest/1606/problem/B
'''

import io, os, sys
input = sys.stdin.readline
output = sys.stdout.write

from math import ceil, log2

# WA
def solve1(N, K):
    res = int(ceil(log2(K)))  # fail K=288230376151711745
    N -= (1 << res)
    if N > 0:
        d, r = divmod(N, K)
        res += d + (r > 0)
        # res += int(ceil(N / K))   # !!!!! floating point err N=10^17, K=1 !!!!!
    return res


def solve2(N, K):
    res = 0
    rem = N - 1
    done = 1
    while rem > 0:
        res += 1
        rem -= done
        done *= 2
        if done > K: break
    if rem > 0:
        d, r = divmod(rem, K)
        res += d + (r > 0)
        # res += int(ceil(rem / K))  # !!!!! floating point err N=10^17, K=1 !!!!!
    return res


solve = solve1

def main():
    T = int(input())
    for _ in range(T):
    	N, K = list(map(int, input().split()))
    	out = solve(N, K)
    	output(str(out) + '\n')


if __name__ == '__main__':
    main()

