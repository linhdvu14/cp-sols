''' E - Average and Median
https://atcoder.jp/contests/abc236/tasks/abc236_e
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write


def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    # mean
    def is_ok_mean(x):
        '''can mean of chosen cards >= x'''
        B = [a-x for a in A]
        dp = [0]*N  # dp[i] = max valid array sum selecting from 0..i that includes i
        for i, b in enumerate(B):
            if i == 0: dp[i] = b
            if i == 1: dp[i] = b + max(0, dp[i-1])
            if i >= 2: dp[i] = b + max(dp[i-1], dp[i-2])
        return dp[-1] >= 1e-7 or dp[-2] >= 1e-7

    mean, lo, hi = -1, 0, max(A)
    for _ in range(30):
        mi = (lo + hi) / 2
        if is_ok_mean(mi):
            mean = mi
            lo = mi
        else:
            hi = mi

    # median
    def is_ok_median(x):
        '''can median of chosen cards >= x'''
        less = geq = cnt = 0
        for a in A:
            if a >= x:
                geq += 1
                less += cnt // 2
                cnt = 0
            else:
                cnt += 1
        less += cnt // 2
        return less < geq

    median, lo, hi = -1, min(A), max(A)
    while lo <= hi:
        mi = (lo + hi) // 2
        if is_ok_median(mi):
            median = mi
            lo = mi + 1
        else:
            hi = mi - 1


    print(f'{mean}\n{median}')


if __name__ == '__main__':
    main()

