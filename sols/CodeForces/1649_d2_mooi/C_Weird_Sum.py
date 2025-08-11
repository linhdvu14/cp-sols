''' C. Weird Sum
https://codeforces.com/contest/1649/problem/C
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') not in [None, '0']

if DEBUG:
    from inspect import currentframe, getframeinfo
    from re import search

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

def solve(R, C, grid):
    def calc(d):
        d.sort()
        res = tot = cnt = pi = 0
        for i in d:
            if cnt > 0:
                tot += (i - pi) * cnt
                res += tot
            cnt += 1
            pi = i
        return res

    color_col = {}
    color_row = {}
    for r in range(R):
        for c in range(C):
            v = grid[r][c]
            if v not in color_col: color_col[v] = []
            if v not in color_row: color_row[v] = []
            color_col[v].append(c)
            color_row[v].append(r)

    res = 0
    for v in color_col.keys():
        res += calc(color_col[v])
        res += calc(color_row[v])

    return res


def main():
    R, C = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(R)]
    out = solve(R, C, grid)
    output(f'{out}\n')


if __name__ == '__main__':
    main()

