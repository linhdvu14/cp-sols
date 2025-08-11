''' C - Connect 6
https://atcoder.jp/contests/abc241/tasks/abc241_c
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

def main():
    N = int(input())
    grid = [input().decode().strip() for _ in range(N)]

    for r in range(N):
        for c in range(N):
            cx = cy = cd1 = cd2 = 0
            for i in range(6):
                if r+i >= N: cx = INF
                elif grid[r+i][c] == '.': cx += 1
                if c+i >= N: cy = INF
                elif grid[r][c+i] == '.': cy += 1
                if r+i >= N or c+i >= N: cd1 = INF
                elif grid[r+i][c+i] == '.': cd1 += 1
                if r+i >= N or c-i < 0: cd2 = INF
                elif grid[r+i][c-i] == '.': cd2 += 1
            if cx <= 2 or cy <= 2 or cd1 <= 2 or cd2 <= 2: return True
    
    return False



if __name__ == '__main__':
    out = main()
    print('Yes' if out else 'No')

