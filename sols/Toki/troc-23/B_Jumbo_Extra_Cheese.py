''' B. Jumbo Extra Cheese
https://tlx.toki.id/contests/troc-23/problems/B
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def solve(N):
    cnt = 0
    for num in range(1, min(N, 10**5)+1):
        p, s = 1, 0
        for d in str(num):
            d = int(d)
            p *= d
            s += d
        if p + s == num: cnt += 1
    return cnt


def main():
    N = int(input())
    out = solve(N)
    print(out)


if __name__ == '__main__':
    main()

