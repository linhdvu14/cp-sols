''' Xor Equation
https://www.codechef.com/NOV21B/problems/XOREQN
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def solve(N, nums):
    MXB = len(bin(max(nums)))
    
    res = 0
    cur = [0]*N
    for j in range(MXB):
        nxt = [0]*N

        ones = 0
        for i, num in enumerate(nums):
            cur[i] += (num >> j) & 1
            if cur[i] > 1:
                cur[i] = 0
                nxt[i] = 1
            ones += cur[i]
        
        if ones % 2 == 1:
            res |= (1 << j)
            for i in range(N):
                if cur[i] == 1:
                    nxt[i] = 1
        cur = nxt    

    return res if sum(cur) == 0 else -1


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        nums = list(map(int, input().split()))
        out = solve(N, nums)
        print(out)


if __name__ == '__main__':
    main()

