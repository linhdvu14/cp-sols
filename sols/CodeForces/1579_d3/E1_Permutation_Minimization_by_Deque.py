''' E1. Permutation Minimization by Deque 
https://codeforces.com/contest/1579/problem/E1
'''

from collections import deque

def solve(nums, N):
    res = deque([])
    for num in nums:
        if not res or num < res[0]:
            res.appendleft(num)
        else:
            res.append(num)
    return ' '.join(map(str, res))
 
def main():
    from sys import stdin
    
    T = int(stdin.readline().strip())
    for _ in range(T):
        N = int(stdin.readline().strip())
        nums = list(map(int, stdin.readline().strip().split()))
        out = solve(nums, N)
        print(out)


if __name__ == '__main__':
    main()
