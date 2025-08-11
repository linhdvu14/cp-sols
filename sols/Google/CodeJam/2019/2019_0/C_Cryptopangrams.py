''' Cryptopangrams 
https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/000000000008830b
'''

def solve(n, l, nums):
    idx = 0
    for i in range(l-1):
        if nums[i] != nums[i+1]:
            idx = i
            break

    primes = [0 for _ in range(l+1)]
    
    primes[idx+1] = gcd(nums[idx], nums[idx+1])
    for i in range(idx+1, l):
        primes[i+1] = nums[i]//primes[i]
    for i in range(idx,-1,-1):
        primes[i] = nums[i]//primes[i+1]

    codes = {p:chr(i+65) for i, p in enumerate(sorted(list(set(primes))))}
    return ''.join(codes[p] for p in primes)


def gcd(a, b): 
    if a == b: return a
    if a == 0: return b
    if b == 0: return a
    if a % 2 == 0 and b % 2 == 0: return gcd(a>>1, b>>1) << 1
    if a % 2 == 0: return gcd(a>>1, b)
    if b % 2 == 0: return gcd(a, b>>1)
    
    if b > a: a, b = b, a
    return gcd((a-b)>>1, b)


def main():
    from sys import stdin
    
    T = int(stdin.readline().strip())

    for t in range(T):
        n, l = list(map(int, stdin.readline().strip().split()))
        nums = list(map(int, stdin.readline().strip().split()))
        out = solve(n, l, nums)
        print('Case #{}: {}'.format(t+1, out))
 
if __name__ == '__main__':
    main()