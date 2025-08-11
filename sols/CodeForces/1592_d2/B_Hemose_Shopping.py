''' B. Hemose Shopping
https://codeforces.com/contest/1592/problem/B
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode() if str
output = sys.stdout.write


def solve(N, X, nums):
    if X==1: return 'YES'

    # unswappable from left/right
    l1, r1 = 0, X-1
    l2, r2 = N-X, N-1

    # overlap is final unswappable range
    l = max(l1, l2)
    r = min(r1, r2)
    if l > r: return 'YES'

    # everything in unswappable range should be in correct order
    snums = sorted(nums)
    for i in range(l, r+1):
        if nums[i] != snums[i]:
            return 'NO'

    return 'YES'


def main():
    T = int(input())
    for _ in range(T):
        N, X = list(map(int, input().split()))
        nums = list(map(int, input().split()))
        out = solve(N, X, nums)
        output(out + '\n')

if __name__ == '__main__':
    main()