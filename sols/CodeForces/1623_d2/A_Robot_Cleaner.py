''' A. Robot Cleaner
https://codeforces.com/contest/1623/problem/A
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write


def solve_simulation(R, C, r1, c1, r2, c2):
    res = 0
    dr = dc = 1
    while not (r1 == r2 or c1 == c2):
        if not 1 <= r1+dr <= R: dr = -dr
        if not 1 <= c1+dc <= C: dc = -dc
        res += 1
        r1 += dr
        c1 += dc
    return res


def solve_projection(R, C, r1, c1, r2, c2):
    mnr = r2 - r1 if r2 >= r1 else 2*R - r1 - r2
    mnc = c2 - c1 if c2 >= c1 else 2*C - c1 - c2
    return min(mnr, mnc)


solve = solve_projection

def main():
    T = int(input())
    for _ in range(T):
        R, C, r1, c1, r2, c2 = list(map(int, input().split()))
        out = solve(R, C, r1, c1, r2, c2)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

