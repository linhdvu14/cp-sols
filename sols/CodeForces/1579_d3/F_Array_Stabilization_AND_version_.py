''' F. Array Stabilization (AND version)
https://codeforces.com/contest/1579/problem/F
'''

def solve_orig(N, D, nums):
    seen = [False]*N
    res = 0
    for i in range(N):
        if seen[i]: continue
        seen[i] = True
        first0 = 0 if nums[i]==0 else -1 # cycle idx of first 0 since i
        last1 = 0 if nums[i]==1 else -1  # cycle idx of start of last 1-block
        mx = 0                           # max steps from any 1 to the next 0 in this cycle
        j, ln = i, 0                     # cur idx, cur cycle len
        while True:
            j = (j+D) % N
            seen[j] = True
            ln += 1
            if nums[j]==1:
                if last1 < 0: 
                    last1 = ln
            else:
                if first0 == -1: first0 = ln
                if last1 != -1: 
                    mx = max(mx, ln-last1)
                    last1 = -1
            if j==i: break               # complete cycle
        
        if last1 != -1:
            if first0 == -1: return -1   # cycle is all 1s
            mx = max(mx, (first0-last1+ln) % ln)
        
        res = max(res, mx)
    
    return res


def solve(N, D, nums):
    seen = [False]*N
    res = 0              # max 1-block over all cycles
    for i in range(N):
        if seen[i]: continue
        orig = i         # orig start idx
        first = -1       # sz of first 1-block
        cnt = 0          # sz of current block
        has_zero = False
        key = -1
        while True:
            i = (i+D) % N
            seen[i] = True
            if nums[i] != key and key != -1:
                if key == 1: res = max(res, cnt)
                if first < 0: first = cnt if key==1 else 0
                cnt = 0
            key = nums[i]
            cnt += 1
            if key==0: has_zero = True
            if i==orig: break
        if key == 1: res = max(res, cnt + first)  
        if not has_zero: return -1

    return res
 
def main():
    from sys import stdin
    
    T = int(stdin.readline().strip())
    for _ in range(T):
        N, D = map(int, stdin.readline().strip().split())
        nums = list(map(int, stdin.readline().strip().split()))
        out = solve(N, D, nums)
        print(out)

if __name__ == '__main__':
    main()
