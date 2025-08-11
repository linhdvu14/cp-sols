''' B - Triple Metre
https://atcoder.jp/contests/abc230/tasks/abc230_b
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write


def main():
    S = input().decode().strip()
    T = 'oxx'*20
    print('Yes' if S in T else 'No')



if __name__ == '__main__':
    main()

