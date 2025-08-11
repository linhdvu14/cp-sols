''' C - Route Map
https://atcoder.jp/contests/abc236/tasks/abc236_c
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write


def main():
    N, M = map(int, input().split())
    S = input().decode().strip().split()
    T = set(input().decode().strip().split())
    res = ['Yes' if s in T else 'No' for s in S]
    print('\n'.join(res))

if __name__ == '__main__':
    main()

