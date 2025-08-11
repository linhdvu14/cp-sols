''' Characteristic Polynomial Verification

https://www.codechef.com/OCT21B/problems/CHARVER

'''
import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode() if str
output = sys.stdout.write

import random
random.seed(123)

MOD = 998244353

# https://en.wikipedia.org/wiki/Freivalds%27_algorithm
def solve(M, N, C, A):
    res = [0]*N  # SUM C[m] * A^m * v
    for _ in range(3):
        v = [random.randint(1,1000) for _ in range(N)]
        for i in range(N): res[i] = C[0]*v[i] % MOD
        for m in range(1,M):            
            v = [sum(A[r][c]*v[c] % MOD for c in range(N)) % MOD for r in range(N)]  # A^m v
            for i in range(N): res[i] = (res[i] + C[m] * v[i]) % MOD
        for x in res:
            if x != 0:
                output('NO\n')
                return
    output('YES\n')


def main():   
    T = int(input())
    for _ in range(T):
        M = int(input())
        C = list(map(int, input().split()))
        N = int(input())
        A = [list(map(int, input().split())) for _ in range(N)]
        solve(M, N, C, A)

if __name__ == '__main__':
    main()


