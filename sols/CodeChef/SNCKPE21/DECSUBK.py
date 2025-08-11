''' Non-Decreasing Subsequence of size K
https://www.codechef.com/SNCKPE21/problems/DECSUBK
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

# https://www.codechef.com/viewsolution/54140938
# https://www.codechef.com/viewsolution/54145157
# https://www.codechef.com/viewsolution/54152228

from bisect import bisect_right

INF = float('inf')

def lis(nums):
    # dp[i] = min num that can be end value of an inc subsequence of length i
    # note dp is strictly increasing
    dp = [INF]*(len(nums)+1)  
    dp[0] = -INF
    
    for num in nums:
        j = bisect_right(dp, num)  # first number > num
        if dp[j-1] <= num < dp[j]:
            dp[j] = num
    for i, v in enumerate(dp):
        if v < INF:
            res = i
    return res


# O(N^3 log N)
def solve1(N, K, nums):
    count = [0]*(N+1)
    for num in nums:
        count[num] += 1

    cands = []
    for num, cnt in enumerate(count):
        if cnt > K: return [-1]
        cands += [num]*cnt

    res = [-1]*N
    for i in range(N):  # place res[i]
        for j, cand in enumerate(cands):
            hi = lis(res[:i] + [cand] + cands[:j] + cands[j+1:])
            lo = lis(res[:i] + [cand] + cands[j+1:][::-1] + cands[:j][::-1])
            if lo <= K <= hi:
                res[i] = cand
                cands = cands[:j] + cands[j+1:]
                break
    return res


# O(N^3)
def solve2(N, K, nums):
    count = [0]*(N+1)
    for num in nums:
        count[num] += 1
    
    if max(count) > K: return [-1]

    res = [-1]*N
    lis = [-1]*N  # lis[i] = length of longest non-dec subseq of res ending at nums[i]
    for i in range(N):  # place res[i]
        for cand, cnt in enumerate(count):
            if cnt == 0: continue

            # lower bound on longest non-deq subseq if set res[i] = cand
            pref = 1
            for j in range(i):
                if res[j] <= cand:
                    pref = max(pref, lis[j]+1)
                        
            suff = max(0, cnt-1)
            for j in range(cand+1, N+1):
                suff = max(suff, count[j])
            
            # if pref + suff > K, then increasing cand will keep pref the same
            # and decrement suff
            if pref + suff <= K:
                res[i] = cand
                lis[i] = pref
                count[cand] -= 1
                break
    
    return res


solve = solve2


def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        nums = list(map(int, input().split()))
        out = solve(N, K, nums)
        print(' '.join(map(str, out)))


if __name__ == '__main__':
    main()

