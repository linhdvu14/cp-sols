''' Yet Another Contest 2 P1 - Betting
https://dmoj.ca/problem/yac2p1
'''

import sys
input = sys.stdin.readline

INF = float('inf')

# -----------------------------------------

# find x, y s.t. xb/a > x + y, yd/c > x + y
# x (b/a - 1) > y -> x / y > a / (b - a)
# y (d/c - 1) > x -> x / y < (d - c) / c
# ok if ac < (b-a)(d-c)

def solve(a, b, c, d):
    return a * c < (b - a) * (d - c)


def main():
    T = int(input())
    for _ in range(T):
        a, b, c, d = list(map(int, input().split()))
        out = solve(a, b, c, d)
        print('YES' if out else 'NO')


if __name__ == '__main__':
    main()

