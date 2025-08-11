''' The Equation 
https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050e02/000000000018fe36
'''
def solve(n,m,nums):
    count_zeros = [0]*50
    count_ones = [0]*50
    for num in nums:
        for i in range(49,-1,-1): 
            b = (num >> i) & 1
            if b == 0: 
                count_zeros[i] += 1
            else: 
                count_ones[i] += 1

    k = 0
    csum = 0
    for i in range(49,-1,-1):
        mn = 0
        for j in range(i-1,-1,-1):
            mn += (1 << j) * min(count_ones[j],count_zeros[j])
        if csum + (1 << i)*count_zeros[i] + mn <= m:
            k = (k << 1) + 1
            csum += (1 << i)*count_zeros[i]
        elif csum + (1 << i)*count_ones[i] + mn <= m:
            k = (k << 1)
            csum += (1 << i)*count_ones[i]
        else:
            return -1
    return k


def main():
    from sys import stdin

    T = int(stdin.readline().strip())
    for t in range(T):
        n, m = list(map(int, stdin.readline().strip().split()))
        nums = list(map(int, stdin.readline().strip().split()))
        out = solve(n,m,nums)
        print('Case #{}: {}'.format(t+1, out))


if __name__ == '__main__':
    main()