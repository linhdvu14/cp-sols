''' An Animal Contest 6 P3 - OAC
https://dmoj.ca/problem/aac6p3
'''

import sys
input = sys.stdin.readline

INF = float('inf')


# pref[r] - pref[l] = (r - l)t
# pref[r] - rt = pref[l] - lt

def solve(N, A):
    MAX = 2 * 10**7 + 5
    pref = [0] * MAX
    res = 0
    for t in range(101):
        s = 0
        pref[0] = 1
        for a in A:
            s += a - t
            res += pref[s]
            pref[s] += 1
        s = 0
        for a in A:
            s += a - t
            pref[s] = 0

    return res


def main():
    N = int(input())
    A = list(map(int, input().split()))
    out = solve(N, A)
    print(out)


if __name__ == '__main__':
    main()

