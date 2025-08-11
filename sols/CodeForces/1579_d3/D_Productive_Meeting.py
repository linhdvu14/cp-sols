''' D. Productive Meeting 
https://codeforces.com/contest/1579/problem/D
'''

from heapq import heappush, heappop

def solve(nums, N):
    h = []
    for i, num in enumerate(nums):
        if num == 0: continue
        heappush(h, (-num, i+1))
    
    k, pairs = 0, []
    while len(h) >= 2:
        n1, i1 = heappop(h)
        n2, i2 = heappop(h)
        pairs.append((i1, i2))
        k += 1
        if n1 < -1: heappush(h, (n1+1, i1))
        if n2 < -1: heappush(h, (n2+1, i2))
    return k, pairs


def main():
    from sys import stdin
    
    T = int(stdin.readline().strip())
    for _ in range(T):
        N = int(stdin.readline().strip())
        nums = list(map(int, stdin.readline().strip().split()))
        k, pairs = solve(nums, N)
        print(k)
        for i,j in pairs:
            print(f'{i} {j}')


if __name__ == '__main__':
    main()
