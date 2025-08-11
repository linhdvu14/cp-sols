''' A - AtCoder Quiz 3
https://atcoder.jp/contests/abc230/tasks/abc230_a
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write


def main():
    N = int(input())
    if N >= 42: N += 1
    print(f'AGC{N:03d}')



if __name__ == '__main__':
    main()

