''' A - Round decimals
https://atcoder.jp/contests/abc226/tasks/abc226_a
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def solve(X):
    ts = X.split('.')
    a, b = int(ts[0]), int(ts[1])
    return a if b < 500 else a + 1


def main():
    X = input().decode().strip()
    out = solve(X)
    output(f'{out}\n')


if __name__ == '__main__':
    main()

