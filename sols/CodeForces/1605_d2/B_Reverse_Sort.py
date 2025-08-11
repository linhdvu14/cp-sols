''' B. Reverse Sort
https://codeforces.com/contest/1605/problem/B
'''

import io, os, sys
from random import randint
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write


def solve(N, S):
    S = list(map(int, list(S)))
    T = sorted(S)
    return [i+1 for i in range(N) if S[i] != T[i]]


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = input().decode().strip()
        out = solve(N, S)
        if len(out) == 0:
            print(0)
        else:
            print(1)
            print(f'{len(out)} ' + ' '.join(map(str, out)))


if __name__ == '__main__':
    main()

