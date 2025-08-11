''' Insider Subsequences
https://www.codechef.com/SNCK1B21/problems/INSIDER
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def solve(N, nums):
    # merge consecutive intervals with same direction
    endpoints = []
    cur = (nums[0], nums[1])
    for i in range(1, N-1):
        nxt = (nums[i], nums[i+1])
        if (nxt[1]-nxt[0])*(cur[1]-cur[0]) >= 0:
            cur = (cur[0], nxt[1])
        else:
            if abs(cur[0] - cur[1]) > 1: 
                if cur[0] > cur[1]:
                    endpoints += [(cur[1]+1, 1), (cur[0]-1, 0), (cur[0], -1)]
                else:
                    endpoints += [(cur[0]+1, 1), (cur[1]-1, 0), (cur[1], -1)]
            cur = nxt
    if abs(cur[0] - cur[1]) > 1: 
        if cur[0] > cur[1]:
            endpoints += [(cur[1]+1, 1), (cur[0]-1, 0), (cur[0], -1)]
        else:
            endpoints += [(cur[0]+1, 1), (cur[1]-1, 0), (cur[1], -1)]
    endpoints.sort()

    # MN[k] = min x s.t. exactly k intervals contain x
    MN = [float('inf')]*(N+1)
    MX = [-float('inf')]*(N+1)

    cnt, px = 0, -1
    for x, d in endpoints:
        if x != px and px != -1:
            MN[cnt] = min(MN[cnt], px)
            MX[cnt] = max(MX[cnt], px)
        px = x
        cnt += d
    MN[cnt] = min(MN[cnt], px)
    MX[cnt] = max(MX[cnt], px)

    # propagate
    for i in range(N-1, -1, -1):
        MN[i] = min(MN[i], MN[i+1])
        MX[i] = max(MX[i], MX[i+1])

    # output
    res_mn, res_mx = [], []
    for k in range(1, N):
        mn, mx = MN[k], MX[k]
        if not -float('inf') < mn < float('inf'): mn = -1
        if not -float('inf') < mx < float('inf'): mx = -1
        res_mn.append(mn)
        res_mx.append(mx)
    
    return res_mn, res_mx


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        nums = list(map(int, input().split()))
        res_mn, res_mx = solve(N, nums)
        output(' '.join(map(str, res_mn)) + '\n')
        output(' '.join(map(str, res_mx)) + '\n')


if __name__ == '__main__':
    main()

