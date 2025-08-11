''' F. ATM and Students
https://codeforces.com/contest/1611/problem/F
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def solve(N, S, A):
    mxi = mxl = -1
    i = 0
    for j in range(N):
        S += A[j]
        if S >= 0 and (j-i+1) > mxl:
            mxi, mxl = i, j-i+1
        while S < 0 and i <= j:
            S -= A[i]
            i += 1
    if mxl <= 0: return [-1]
    return [mxi+1, mxi+mxl]


def main():
    T = int(input())
    for _ in range(T):
        N, S = list(map(int, input().split()))
        A = list(map(int, input().split()))
        out = solve(N, S, A)
        print(' '.join(map(str, out)))


if __name__ == '__main__':
    main()

