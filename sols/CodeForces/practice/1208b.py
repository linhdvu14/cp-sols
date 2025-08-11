def solve1(nums, n):  # O(n^2)
    dl = set()
    mx = 0

    for il, xl in enumerate(nums):
        dr = set()
        for ir, xr in enumerate(nums[::-1]):
            if ir+il >= n-1 or xr in dr or xr in dl: break
            dr.add(xr)
        if xl in dl:
            mx = max(mx, len(dl)+len(dr))
            break
        if xl not in dr:
            mx = max(mx, len(dl)+len(dr)+1)
        else:
            mx = max(mx, len(dl)+len(dr))
        dl.add(xl)

    return n-mx


# 1 2 4 4 1 2 5 5 1
def solve2(nums, n):  # O(n): longest subarray with no dup
    last = {}  # val -> last idx
    mx = 0
    i = 0
    for j, num in enumerate(nums+nums):
        if num in last:
            i = max(i,last[num]+1)
        last[num] = j
        if i==0 or j==n-1 or (0<i<n and n<=j): mx = max(mx, j-i+1)
    return n-mx


solve = solve2


def main():
    from sys import stdin
    n = int(stdin.readline().strip())
    nums = list(map(int,stdin.readline().strip().split()))
    print(solve(nums, n))
 

if __name__ == '__main__':
    main()