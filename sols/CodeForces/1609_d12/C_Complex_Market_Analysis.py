''' C. Complex Market Analysis
https://codeforces.com/contest/1609/problem/C
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

INF = float('inf')

def sieve(n):
    primes = set([])
    leastPrimeFactor = [0]*(n+1)
    for i in range(2,n+1):
        if leastPrimeFactor[i] == 0:
            primes.add(i)
            leastPrimeFactor[i] = i
        for p in primes:
            if p > leastPrimeFactor[i] or p*i > n: break
            leastPrimeFactor[p*i] = p  # once per composite number
    return primes

primes = sieve(10**6 + 1)


def solve(N, E, A):
    res = 0
    for i in range(E):
        for j in range(i, N, E):
            if A[j] not in primes: continue
            left = right = 0
            for k in range(j-E, -1, -E):
                if A[k] != 1: break
                left += 1
            for k in range(j+E, N, E):
                if A[k] != 1: break
                right += 1
            res += left + right + left*right

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, E = list(map(int, input().split()))
        A = list(map(int, input().split()))
        out = solve(N, E, A)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

