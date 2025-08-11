''' Product Pain
https://www.codechef.com/SNCKPE21/problems/PRDTPAIN
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write


def solve(N, nums):
    res = 0
    for i in range(N):
        for j in range(i+2, N):
            target = (nums[i] + nums[j]) / 2
            idx, lo, hi = -1, i, j
            while lo <= hi:
                mi = (lo + hi) // 2
                if nums[mi] <= target:
                    idx = mi
                    lo = mi + 1
                else:
                    hi = mi - 1
            add = 0
            if i < idx < j: add = max(add, (nums[i] - nums[idx]) * (nums[idx] - nums[j]))
            if i < idx+1 < j: add = max(add, (nums[i] - nums[idx+1]) * (nums[idx+1] - nums[j]))
            res += add

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        nums = list(map(int, input().split()))
        out = solve(N, nums)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

