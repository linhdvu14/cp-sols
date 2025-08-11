''' Equal Coins
https://www.codechef.com/NOV21B/problems/EQUALCOIN
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def solve(X, Y):
    if X == 0: return Y % 2 == 0
    return X % 2 == 0


def main():
    T = int(input())
    for _ in range(T):
        X, Y = list(map(int, input().split()))
        out = solve(X, Y)
        print('YES' if out else 'NO')


if __name__ == '__main__':
    main()

