''' D - Teleportation
https://atcoder.jp/contests/abc226/tasks/abc226_d
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write


def gcd(a, b):  # assume non-neg
    if a < b: a, b = b, a
    while b > 0: a, b = b, a%b
    return a


def main():
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]
    pool = set()
    for i in range(N):
        x1, y1 = points[i]
        for j in range(i+1, N):
            x2, y2 = points[j]
            d1, d2 = x1-x2, y1-y2
            g = gcd(abs(d1), abs(d2))
            pool.add((d1//g, d2//g))
            pool.add((-d1//g, -d2//g))
    print(len(pool))

if __name__ == '__main__':
    main()

