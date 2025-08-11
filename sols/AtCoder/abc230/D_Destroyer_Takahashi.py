''' D - Destroyer Takahashi
https://atcoder.jp/contests/abc230/tasks/abc230_d
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write


def main():
    N, D = list(map(int, input().strip().split()))
    intervals = [tuple(map(int, input().strip().split())) for _ in range(N)]
    intervals.sort(key=lambda tup: (tup[1], tup[0]))

    res = 0
    i = 0
    while i < N:
        res += 1
        l, r = intervals[i][1], intervals[i][1]+D-1
        i += 1
        while i < N and max(intervals[i][0], l) <= min(intervals[i][1], r):
            i += 1
    print(res)


if __name__ == '__main__':
    main()

