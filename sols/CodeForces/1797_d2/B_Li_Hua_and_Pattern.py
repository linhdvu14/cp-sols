''' B. Li Hua and Pattern
https://codeforces.com/contest/1797/problem/B
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def debug(*args):   
    if os.environ.get('debug') in [None, '0']: return
    from inspect import currentframe, getframeinfo
    from re import search
    frame = currentframe().f_back
    s = getframeinfo(frame).code_context[0]
    r = search(r"\((.*)\)", s).group(1)
    vnames = r.split(', ')
    var_and_vals = [f'{var}={val}' for var, val in zip(vnames, args)]
    prefix = f'{currentframe().f_back.f_lineno:02d}: '
    print(f'{prefix}{", ".join(var_and_vals)}')

INF = float('inf')

# -----------------------------------------

def solve(N, K, grid):
    diff = 0
    for r in range(N):
        for c in range(N):
            if grid[r][c] != grid[N - 1 - r][N - 1 - c]:
                diff += 1
    diff //= 2
    if diff > K: return 'NO'
    if (K - diff) % 2 == 1 and N % 2 == 0: return 'NO'
    return 'YES'


def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        grid = [list(map(int, input().split())) for _ in range(N)]
        res = solve(N, K, grid)
        print(res)


if __name__ == '__main__':
    main()

