''' Games of Wasseypur
https://www.codechef.com/CSNS21B/problems/GAMEW
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def solve(N, S):
    cnt = 0
    pc = ''
    for c in S:
        if c != pc and pc != '':
            cnt += 1
        pc = c
    cnt += 1
    return 'RAMADHIR' if cnt % 3 == 2 else 'SAHID'


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = input().decode().strip()
        out = solve(N, S)
        print(out)


if __name__ == '__main__':
    main()

