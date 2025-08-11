''' D. Big Brush
https://codeforces.com/contest/1638/problem/D
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

def solve():
    R, C = list(map(int, input().split()))
    V = [list(map(int, input().split())) for _ in range(R)]
    res = []

    # used = will be colored over
    used = [[0]*C for _ in range(R)]

    # queue holds used cells
    stack = []
    for r in range(R-1):
        for c in range(C-1):
            if V[r][c] == V[r][c+1] == V[r+1][c] == V[r+1][c+1]:
                res.append((r, c, V[r][c]))
                used[r][c] = used[r][c+1] = used[r+1][c] = used[r+1][c+1] = 1
                stack += [(r, c), (r, c+1), (r+1, c), (r+1, c+1)]
    
    # try coloring 2x2 block containing an used cell
    while stack:
        r, c = stack.pop()
        for nr, nc in [(r-1, c-1), (r-1, c), (r, c-1), (r, c)]:
            if not (0 <= nr < R-1 and 0 <= nc < C-1): continue
            vals = []
            for nr2, nc2 in [(nr, nc), (nr, nc+1), (nr+1, nc), (nr+1, nc+1)]:
                if used[nr2][nc2]: continue
                vals.append(V[nr2][nc2])
            if len(set(vals)) == 1:
                res.append((nr, nc, vals[0]))
                for nr2, nc2 in [(nr, nc), (nr, nc+1), (nr+1, nc), (nr+1, nc+1)]:
                    if used[nr2][nc2]: continue
                    used[nr2][nc2] = 1
                    stack.append((nr2, nc2))

    cnt = sum(sum(row) for row in used)
    if cnt < R*C:
        print(-1)
    else:
        print(len(res))
        res = [str(r+1) + ' ' + str(c+1) + ' ' + str(v) for r, c, v in res[::-1]]
        print('\n'.join(res))


if __name__ == '__main__':
    solve()

