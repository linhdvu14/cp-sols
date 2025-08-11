''' An Animal Contest 6 P2 - G-Pop
https://dmoj.ca/problem/aac6p2
'''

import sys
input = sys.stdin.readline

INF = float('inf')


def main():
    N, Q = list(map(int, input().split()))
    if Q == 0: return 1, [1] * N

    intervals = []
    for _ in range(Q):
        l, r = map(int, input().split())
        intervals.append((l-1, r-1))
    intervals.sort()

    K = max(r - l + 1 for l, r in intervals)

    merged_intervals = []
    pl, pr = intervals[0]
    for l, r in intervals[1:]:
        if l > pr:
            merged_intervals.append((pl, pr))
            pl, pr = l, r
        else:
            pr = max(pr, r)
    merged_intervals.append((pl, pr))

    order = [0] * N
    ptr = last = 0
    for l, r in merged_intervals:
        for j in range(last, l+1):
            order[j] = order[last]
        for j in range(l+1, r+1):
            order[j] = ptr = (ptr + 1) % K
        last = r
    
    for j in range(last+1, N): 
        order[j] = order[last]

    order = [x+1 for x in order]
    return K, order



if __name__ == '__main__':
    a, b = main()
    print(a)
    print(*b)

