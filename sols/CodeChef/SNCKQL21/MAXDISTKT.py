''' Maximum Number Of Distinct Elements
https://www.codechef.com/SNCKQL21/problems/MAXDISTKT
'''


import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def solve(N, nums):
    count = [[] for _ in range(N+1)]
    for i, n in enumerate(nums): 
        count[n].append(i)

    res = [0]*N
    cur = 0
    for num, indices in enumerate(count):
        for i in indices:
            if cur >= num: break
            res[i] = cur
            cur += 1

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

