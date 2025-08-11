''' C. I Got Fives
https://tlx.toki.id/contests/troc-23/problems/C
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

# let P[n] = a0 * 5^0 + a1 * 5^1 + a2 * 5^2 + ... + an * 5^n
# need to represent N = P[n] where ai = 0, 1, -1
# i.e. represent N + 5^0 + 5^1 + ... + 5^n = P[n] where ai = 0, 1, 2
# note n <= 21 as 5^22 - 5^21 - 5^20 - ... - 5^0 > 10**15 (or just 5^22 > 1e15)

def solve(N):
    P = [1]
    N += 1
    while P[-1] < 10**15:
        P.append(P[-1] * 5)
        N += P[-1]

    while P:
        p = P.pop()
        b, N = divmod(N, p)
        if b > 2: return 'NO'
    
    return 'YES'


def main():
    N = int(input())
    out = solve(N)
    print(out)


if __name__ == '__main__':
    main()
