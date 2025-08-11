''' Problem A1: Ready, Go (Part 1)
https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-2/problems/A1
'''

import os, sys
input = sys.stdin.readline
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

def solve(R, C, grid):
    vis = [[0] * C for _ in range(R)]
    scores = {}

    for r in range(R):
        for c in range(C):
            if vis[r][c] or grid[r][c] != 'W': continue
            cnt = 0
            st = [(r, c)]
            vis[r][c] = 1
            border = set()
            while st:
                r1, c1 = st.pop()
                cnt += 1
                for r2, c2 in [(r1 - 1, c1), (r1 + 1, c1), (r1, c1 - 1), (r1, c1 + 1)]:
                    if not (0 <= r2 < R and 0 <= c2 < C): continue
                    if vis[r2][c2] or grid[r2][c2] == 'B': continue
                    if grid[r2][c2] == '.': border.add((r2, c2)); continue
                    vis[r2][c2] = 1
                    st.append((r2, c2))
            if len(border) == 1:
                r, c = border.pop()
                scores[(r, c)] = scores.get((r, c), 0) + cnt

    return 'YES' if scores else 'NO'


def main():
    T = int(input())
    for t in range(T):
        R, C = list(map(int, input().split()))
        grid = [input().strip() for _ in range(R)]
        res = solve(R, C, grid)
        print(f'Case #{t+1}: {res}')


if __name__ == '__main__':
    main()

