''' Hill Sequence
https://www.codechef.com/NOV21B/problems/HILLSEQ
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

from collections import deque

def solve(N, nums):
    nums.sort(reverse=True)
    res = deque([])

    def update(val, cnt):
        if cnt > 2: return False
        if cnt == 2 and len(res) == 0: return False
        res.append(val)
        if cnt == 2: res.appendleft(val)
        return True

    cnt = prev = 0
    for num in nums:
        if num != prev and prev != 0:
            ok = update(prev, cnt)
            if not ok: return [-1]
            cnt = 0
        prev = num
        cnt += 1
    ok = update(prev, cnt)
    if not ok: return [-1]

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        nums = list(map(int, input().split()))
        out = solve(N, nums)
        print(' '.join(map(str, out)))


if __name__ == '__main__':
    main()

