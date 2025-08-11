''' B - Who is missing?
https://atcoder.jp/contests/abc236/tasks/abc236_b
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write


def main():
    N = int(input())
    A = map(int, input().split())
    cnt = [0]*N
    for a in A: cnt[a-1] += 1
    for a, cnt in enumerate(cnt):
        if cnt == 3: 
            print(a+1)
            break

if __name__ == '__main__':
    main()

