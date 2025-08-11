''' Cheerio Contest 3 P1 - Wet Floor
https://dmoj.ca/problem/cheerio3p1
'''

import os, sys
input = sys.stdin.readline  # strip() if str

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

def main():
    R, C = list(map(int, input().split()))

    grid = [list(input().strip()) for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'W': continue
            for nr, nc in [[r, c + 1], [r, c - 1], [r + 1, c], [r - 1, c]]:
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 'W':
                    grid[r][c] = 'C'
                    break

    for row in grid: print(*row, sep='')


if __name__ == '__main__':
    main()

