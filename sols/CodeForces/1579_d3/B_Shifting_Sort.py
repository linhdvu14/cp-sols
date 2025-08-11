''' B. Shifting Sort 
https://codeforces.com/contest/1579/problem/B
'''

def solve(nums, N):
    res = []
    for i in range(N):
        mni, mnv = i, nums[i]
        for j in range(i+1, N):
            if nums[j] < mnv: 
                mni, mnv = j, nums[j]
        if mni==i: continue
        res.append((i, mni, mni-i))
        nums[i:mni+1] = [nums[mni]] + nums[i:mni]
    return res           
    
def main():
    from sys import stdin
    
    T = int(stdin.readline().strip())
    for _ in range(T):
        N = int(stdin.readline().strip())
        nums = list(map(int, stdin.readline().strip().split()))
        out = solve(nums, N)
        print(len(out))
        for l,r,d in out:
            print(f'{l+1} {r+1} {d}')
    
if __name__ == '__main__':
    main()