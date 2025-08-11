''' An Animal Contest 6 P1 - Workout Routine
https://dmoj.ca/problem/aac6p1
'''

import sys
input = sys.stdin.readline

INF = float('inf')


def solve(N, K):
    res = list(range(1, N+1))
    S = N * (N+1) // 2
    add = ((S + K - 1) // K) * K - S
    res[-1] += add
    if res[-1] > 10**9: return [-1]
    return res


def main():
    N, K = list(map(int, input().split()))
    out = solve(N, K)
    print(*out)


if __name__ == '__main__':
    main()

