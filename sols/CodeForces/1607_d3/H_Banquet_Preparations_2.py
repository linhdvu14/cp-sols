''' H. Banquet Preparations 2
https://codeforces.com/contest/1607/problem/H
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

# let taster eat ma_i of fish from each dish (a_i, b_i)
# then max(0, M-b_i) <= ma_i <= min(a_i, M)
# then each rem_i is an interval: a_i - min(a_i, M)..a_i - max(0, M-b_i)
# --> within each candidate group, find min num sets s.t. all intervals in a set have a common point
def solve(N, dishes):
    res_c = 0
    res_a = [0]*N

    def solve_group(intervals):
        nonlocal res_c
        intervals.sort()
        p = intervals[0][0]
        res_c += 1
        for hi, lo, i in intervals:                
            if not (lo <= p <= hi):
                p = hi
                res_c += 1
            res_a[i] = dishes[i][0] - p

    groups = {}
    for i, (a, b, m) in enumerate(dishes):
        r = a + b - m
        if r not in groups: groups[r] = []
        lo = max(0, a-m)
        hi = min(a, a+b-m)
        groups[r].append((hi, lo, i))
    
    for group in groups.values():
        solve_group(group)

    print(res_c)
    for i, ma in enumerate(res_a):
    	print(f'{ma} {dishes[i][2]-ma}')


def main():
    T = int(input())
    for _ in range(T):
        _ = input()
        N = int(input())
        dishes = [tuple(map(int, input().split())) for _ in range(N)]
        solve(N, dishes)


if __name__ == '__main__':
    main()

