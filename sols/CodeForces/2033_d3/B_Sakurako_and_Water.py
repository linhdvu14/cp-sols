''' B. Sakurako and Water
https://codeforces.com/contest/2033/problem/B
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

from inspect import currentframe, getframeinfo
from re import search
DEBUG = os.environ.get('debug') not in [None, '0']

def debug(*args):   
    if not DEBUG: return
    frame = currentframe().f_back
    s = getframeinfo(frame).code_context[0]
    r = search(r"\((.*)\)", s).group(1)
    vnames = r.split(', ')
    var_and_vals = [f'{var}={val}' for var, val in zip(vnames, args)]
    prefix = f'{currentframe().f_back.f_lineno:02d}: '
    print(f'{prefix}{", ".join(var_and_vals)}')

INF = float('inf')

# -----------------------------------------

def solve(N, grid):
    res = 0
    for i in range(N):
        starts = list(set([(i, 0), (0, i)]))
        for r, c in starts:
            mx = 0
            for _ in range(N):
                if r == N or c == N: break
                if grid[r][c] < 0: mx = max(mx, -grid[r][c])
                r += 1
                c += 1
            res += mx

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        grid = [list(map(int, input().split())) for _ in range(N)]
        res = solve(N, grid)
        print(res)


if __name__ == '__main__':
    main()

