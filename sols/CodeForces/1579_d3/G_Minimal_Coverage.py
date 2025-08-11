''' G. Minimal Coverage
https://codeforces.com/contest/1579/problem/G
'''

def solve_dp(N, nums):
    MAX = max(nums)*2 + 1

    # process segments left to right
    # l = dist from cur endpoint to coverage left opening
    # cur[l] = r = min dist from cur endpoint to coverage right opening
    cur = [0]*MAX
    for d in nums:
        nxt = [MAX]*MAX
        for l, r in enumerate(cur):
            if l+d < MAX: nxt[l+d] = min(nxt[l+d], max(r-d, 0))  # right: 0 -> l -> l+r / end
            if r+d < MAX: nxt[r+d] = min(nxt[r+d], max(l-d, 0))  # left: 0 -> r -> l+r / end
        cur = nxt
    return min(l+r for l,r in enumerate(cur))


def solve_bisect(N, nums): 
    def is_ok(L):  # can coverage size <= L
        # dp[i] = can current endpoint lie at i
        dp = mask = (1 << (L+1)) - 1

        # can end at i if previous ends at i-d or i+d
        for d in nums:
            dp = ((dp << d) | (dp >> d)) & mask
        
        return dp != 0

    res, lo, hi = -1, max(nums), max(nums)*2
    while lo <= hi:
        mi = (lo+hi) // 2
        if is_ok(mi):
            res = mi
            hi = mi-1
        else:
            lo = mi+1
    return res

solve = solve_bisect

def main():
    from sys import stdin
    
    T = int(stdin.readline().strip())
    for _ in range(T):
        N = int(stdin.readline().strip())
        nums = list(map(int, stdin.readline().strip().split()))
        out = solve(N, nums)
        print(out)

if __name__ == '__main__':
    main()
