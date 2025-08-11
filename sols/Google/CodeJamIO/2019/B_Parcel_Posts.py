''' Parcel Posts 
https://codingcompetitions.withgoogle.com/codejamio/round/0000000000050fc5/0000000000054e9a
'''

def solve(nums):
    if len(nums) < 2:
        return 0

    out = 0
    sign = 0
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            continue

        csign = 1 if nums[i] > nums[i-1] else -1
        if sign == 0 or sign == csign:
            sign = csign
            continue
        
        # meet inflection point
        out += 1
        sign = 0

    # don't count rightmost post
    return out - 1



def main():
    from sys import stdin
    
    T = int(stdin.readline().strip())

    for t in range(T):
        K = int(stdin.readline().strip())
        heights = [int(h) for h in stdin.readline().strip().split()]
        out = solve(heights)
        print('Case #{}: {}'.format(t + 1, out))
    
 
if __name__ == '__main__':
    main()