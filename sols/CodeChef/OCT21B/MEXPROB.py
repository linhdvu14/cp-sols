''' Yet another MEX problem

https://www.codechef.com/OCT21B/problems/MEXPROB

'''
import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
output = sys.stdout.write

def solve(N, K, nums):
    # how many subarrays contain 0..x-1 i.e. have MEX >= x
    def count(x):
        geq = i = sz = 0
        counter = [0]*x
        for j, num in enumerate(nums):
            if num < x: 
                if counter[num] == 0: sz += 1
                counter[num] += 1

            # last i where nums[i..j] doesn't contain 0..x-1
            while i <= j and sz == x:
                if nums[i] < x: 
                    counter[nums[i]] -= 1
                    if counter[nums[i]] == 0: sz -= 1
                i += 1
            
            # all nums[k..j] where k < i contain 0..x-1
            geq += i

        return geq

    # min x s.t. at least K subarrays have MEX < x, i.e. count(x+1) <= num_subarrays - K
    target = N*(N+1) // 2 - K
    lo, hi = 0, max(nums)+2
    while lo <= hi:
        mi = (lo+hi) // 2
        if count(mi) <= target:
            hi = mi-1
        else:
            lo = mi+1
    
    return hi


def main():   
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        nums = list(map(int, input().split()))
        out = solve(N, K, nums)
        output(str(out) + '\n')



if __name__ == '__main__':
    main()


