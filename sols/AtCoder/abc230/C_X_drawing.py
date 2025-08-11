''' C - X drawing
https://atcoder.jp/contests/abc230/tasks/abc230_c
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def main():
    N, A, B = list(map(int, input().strip().split()))
    P, Q, R, S = list(map(int, input().strip().split()))
        
    res = [['.']*(S-R+1) for _ in range(Q-P+1)]

    l = max(1-A, 1-B, P-A, R-B)
    r = min(N-A, N-B, Q-A, S-B)
    for k in range(l, r+1):
        i, j = A+k-P+1, B+k-R+1
        res[i-1][j-1] = '#'

    l = max(1-A, B-N, P-A, B-S)
    r = min(N-A, B-1, Q-A, B-R)
    for k in range(l, r+1):
        i, j = A+k-P+1, B-k-R+1
        res[i-1][j-1] = '#'

    for row in res: print(''.join(row))


if __name__ == '__main__':
    main()
