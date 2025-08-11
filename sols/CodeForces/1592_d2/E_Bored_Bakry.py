''' E. Bored Bakry
https://codeforces.com/contest/1592/problem/E
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode() if str
output = sys.stdout.write


# let nums[l..r] be good i.e. AND(nums[l]..nums[r]) > XOR(nums[l]..nums[r])
# then r-l+1 must be even, otherwise all bits set in AND(l, r) is also set in XOR(l, r)
# let k be the highest set bit of AND(l, r), then k is unset in XOR(l, r)
# thus bits 20..k-1 of XOR(l, r) must be zeros
# ---> find max r-l+1 for each k=0..20 s.t.
# 1) r-l+1 is even
# 2) k is all set in nums[l..r]
# 3) XOR(l, r) >> k == 0 i.e. XOR(0, r) >> k == XOR(0, l-1) >> k
def solve(N, nums):
    res = 0
    for _ in range(20):
        starts = [{}, {0: -1}]  # xor prefix -> first odd/even idx in current 1-block
        pref = 0                # cumulative prefix xor
        for i in range(N):
            k_bit = nums[i] & 1
            nums[i] >>= 1
            if k_bit == 0:      # exit 1-block, restart
                starts = [{0: i}, {}] if i%2==0 else [{}, {0: i}]
                pref = 0
            else:
                pref ^= nums[i]
                if pref not in starts[i%2]: starts[i%2][pref] = i
                res = max(res, i - starts[i%2][pref])
    return res


def main():
    N = int(input())
    nums = list(map(int, input().split()))
    out = solve(N, nums)
    output(str(out) + '\n')

if __name__ == '__main__':
    main()