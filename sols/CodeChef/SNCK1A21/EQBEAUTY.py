''' Equal Beauty
https://www.codechef.com/SNCK1A21/problems/EQBEAUTY
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def solve(N, nums):
    if N == 2: return 0
    nums.sort()

    # min cost to make nums[lo..hi] the same value
    def cost_eq(lo, hi):
        if lo > hi: return 0
        M = hi-lo+1
        res = cur = sum(nums[lo:hi+1]) - nums[lo]*M  # all equal nums[lo]
        for i in range(1, M):                        # all equal nums[lo+i]
            d = nums[lo+i] - nums[lo+i-1]
            cur += d*i - d*(M-i)
            res = min(res, abs(cur))
        return res

    # find rightmost j s.t. min abs(val-nums[j]) and nums[j] <= val
    def search_leq(val):
        j = -1
        lo, hi = 0, N-1
        while lo <= hi:
            mi = (lo+hi) // 2
            if nums[mi] <= val:
                j = mi
                lo = mi + 1
            else:
                hi = mi - 1
        return j
    
    # case #1: nums[0] or nums[-1] in its own partition
    # the other partition must all have same value
    lo, hi = 1, N-2
    while lo < N and nums[lo] == nums[lo-1]: lo += 1
    while hi >= 0 and nums[hi] == nums[hi+1]: hi -= 1
    res = min(cost_eq(lo, N-1), cost_eq(0, hi))

    # case #2: nums[0] and nums[-1] in different partitions
    # let partitions have range (nums[0]..nums[i]) and (nums[j]..nums[-1]) for some index 0 < i != j < N-1
    # then cost is abs(nums[-1]+nums[0]-nums[j]-nums[i])
    # consider each possible pairing (0, i), where i is leftmost occurrence of value nums[i]
    # find rightmost j s.t. nums[j] is closest to nums[-1]+nums[0]-nums[i]
    for i in range(1, N-1):
        if nums[i] == nums[i-1]: continue  # only consider leftmost occurrence
        target = nums[0] + nums[-1] - nums[i]
        j = search_leq(target)
        if j == -1:                        # all nums > target, pick smallest
            j = 2 if i==1 else 1
            res = min(res, abs(target - nums[j]))
        else: 
            # try leq
            j1 = j if j != i else j-1
            if j1 != 0: res = min(res, abs(target - nums[j1]))
            # try geq
            j2 = j+1 if j+1 != i else j+2
            if j2 < N-1: res = min(res, abs(target - nums[j2]))

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        nums = list(map(int, input().split()))
        out = solve(N, nums)
        print(out)


if __name__ == '__main__':
    main()

