''' Add and Divide
https://www.codechef.com/START13B/problems/ADDNDIV
'''

def sieve(n):
    primes = []
    leastPrimeFactor = [0]*(n+1)
    for i in range(2,n+1):
        if leastPrimeFactor[i] == 0:
            primes.append(i)
            leastPrimeFactor[i] = i
        for p in primes:
            if p > leastPrimeFactor[i] or p*i > n: break
            leastPrimeFactor[p*i] = p  # once per composite number
    return primes

primes = sieve(10**5)

def factorize(n):
    if n < 2: return []
    res = []
    i = 0
    while primes[i]*primes[i] <= n:
        cnt = 0
        while n % primes[i] == 0:
            cnt += 1
            n //= primes[i]
        if cnt: res.append(primes[i])
        i += 1
    if n > 1: res.append(n)
    return res

# can some multiple of a be a power of b
# does b include all prime factors of a
def solve(a, b):
    if a==1: return True
    factors = factorize(a)
    for p in factors:
        if p>b or b%p != 0: return False
    return True


def main():
    from sys import stdin
    
    T = int(stdin.readline().strip())
    for _ in range(T):
        a, b = list(map(int,stdin.readline().strip().split()))
        out = solve(a, b)
        print('YES' if out else 'NO')


if __name__ == '__main__':
    main()

