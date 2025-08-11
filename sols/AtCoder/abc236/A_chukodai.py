''' A - chukodai
https://atcoder.jp/contests/abc236/tasks/abc236_a
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write


def main():
    S = list(input().decode().strip())
    a, b = list(map(int, input().split()))
    S[a-1], S[b-1] = S[b-1], S[a-1]
    print(''.join(S))

if __name__ == '__main__':
    main()

