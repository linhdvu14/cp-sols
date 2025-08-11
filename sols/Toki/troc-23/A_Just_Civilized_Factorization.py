''' A. Just & Civilized Factorization
https://tlx.toki.id/contests/troc-23/problems/A
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def solve(N):
    cnt = 0
    for d in range(1, N+1):
        if N % d == 0:
            cnt += 1
    return 'YES' if cnt==5 else 'NO'


def main():
    N = int(input())
    out = solve(N)
    print(out)


if __name__ == '__main__':
    main()