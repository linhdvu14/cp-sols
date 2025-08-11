''' Problem 2. Robot Instructions
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
    X, Y = map(int, input().split())
    vals = [tuple(map(int, input().split())) for _ in range(N)]

    res = [0] * (N+1)

    # left sums
    left = {}
    def dfs1(sz, cx, cy, i, hi):
        if i >= hi:
            if (cx, cy) not in left: left[cx, cy] = {}
            if sz not in left[cx, cy]: left[cx, cy][sz] = 0
            left[cx, cy][sz] += 1
        else:
            dfs1(sz, cx, cy, i+1, hi)
            dfs1(sz+1, cx + vals[i][0], cy + vals[i][1], i+1, hi)
    dfs1(0, 0, 0, 0, N//2)

    # right sums
    def dfs2(sz, cx, cy, i, hi):
        if i >= hi:
            # meet in the middle
            dx, dy = X - cx, Y - cy
            if (dx, dy) in left:
                for szl, cnt in left[dx, dy].items():
                    res[sz + szl] += cnt
        else:
            dfs2(sz, cx, cy, i+1, hi)
            dfs2(sz+1, cx + vals[i][0], cy + vals[i][1], i+1, hi)
    dfs2(0, 0, 0, N//2, N)
    
    print('\n'.join(map(str, res[1:])))


if __name__ == '__main__':
    main()

