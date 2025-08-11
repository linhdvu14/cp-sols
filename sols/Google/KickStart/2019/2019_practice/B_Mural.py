''' Mural 
https://codingcompetitions.withgoogle.com/kickstart/round/0000000000051060/0000000000058b89
'''
# max-sum subsubsequence S1-E1 of length (N+1) // 2
# can always paint S1-E1 if start at O: S----S1----O--E1--E


def solve(n, nums):
    ln = (n+1) // 2
    out = curr = sum(nums[:ln])
    for i in range(ln, n):
        curr = curr - nums[i-ln] + nums[i]
        out = max(out, curr)
    return out


def main():
    from sys import stdin, stdout, stderr
    
    T = int(stdin.readline().strip())

    for t in range(T):
        n = int(stdin.readline().strip())
        nums = list(map(int, list(stdin.readline().strip())))
        out = solve(n, nums)
        print('Case #{}: {}'.format(t+1, out))

 
if __name__ == '__main__':
    main()