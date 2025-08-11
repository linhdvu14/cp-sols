''' D. Blue-Red Permutation
https://codeforces.com/contest/1607/problem/D
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def solve(N, vals, colors):
    left, right = [], []
    for i, val in enumerate(vals):
        if colors[i] == 'B':
            left.append(val)
        else:
            right.append(val)
    left.sort()
    right.sort()
    if any(val < i+1 for i, val in enumerate(left)): return 'NO'
    if any(val > i+1+len(left) for i, val in enumerate(right)): return 'NO'
    return 'YES' 


# WA: 2 2 2 7 / RRRB
def solve_wa1(N, vals, colors):
    intervals = []  # (end, start)
    for i, val in enumerate(vals):
        if colors[i] == 'B':
            if val < 1: return 'NO'
            intervals.append((val, 1))
        else:
            if val > N: return 'NO'
            intervals.append((N, val))
    intervals.sort()

    for i, (end, start) in enumerate(intervals):
        if not start <= i+1 <= end: return 'NO'

    return 'YES'


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        vals = list(map(int, input().split()))
        colors = input().decode().strip()
        out = solve(N, vals, colors)
        output(str(out) + '\n')


if __name__ == '__main__':
    main()

