''' F - Skate
https://atcoder.jp/contests/abc241/tasks/abc241_f
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

from collections import deque

def main():
    R, C, N = list(map(int, input().split()))
    SX, SY = list(map(int, input().split()))
    GX, GY = list(map(int, input().split()))
    SX, SY, GX, GY = SX-1, SY-1, GX-1, GY-1

    conn_rows, conn_cols = {}, {}
    for _ in range(N):
        r, c = list(map(int, input().split()))
        if r-1 not in conn_rows: conn_rows[r-1] = []
        if c-1 not in conn_cols: conn_cols[c-1] = []
        conn_rows[r-1].append(c-1)
        conn_cols[c-1].append(r-1)
    
    for v in conn_rows.values(): v.sort()
    for v in conn_cols.values(): v.sort()
    
    # bfs
    seen = set((r, c))
    queue = deque([(SX, SY, 0)])
    while queue:
        r, c, d = queue.popleft()
        if r == GX and c == GY: return d
        if r in conn_rows:
            idx, lo, hi = -1, 0, len(conn_rows[r])-1
            while lo <= hi:
                mi = (lo + hi) // 2
                if conn_rows[r][mi] < c:
                    idx = mi
                    lo = mi + 1
                else:
                    hi = mi - 1
            if 0 <= idx < len(conn_rows[r]) and (r, conn_rows[r][idx]+1) not in seen:
                seen.add((r, conn_rows[r][idx]+1))
                queue.append((r, conn_rows[r][idx]+1, d+1))
            if 0 <= idx+1 < len(conn_rows[r]) and (r, conn_rows[r][idx+1]-1) not in seen:
                seen.add((r, conn_rows[r][idx+1]-1))
                queue.append((r, conn_rows[r][idx+1]-1, d+1))
        if c in conn_cols:
            idx, lo, hi = -1, 0, len(conn_cols[c])-1
            while lo <= hi:
                mi = (lo + hi) // 2
                if conn_cols[c][mi] < r:
                    idx = mi
                    lo = mi + 1
                else:
                    hi = mi - 1
            if 0 <= idx < len(conn_cols[c]) and (conn_cols[c][idx]+1, c) not in seen:
                seen.add((conn_cols[c][idx]+1, c))
                queue.append((conn_cols[c][idx]+1, c, d+1))
            if 0 <= idx+1 < len(conn_cols[c]) and (conn_cols[c][idx+1]-1, c) not in seen:
                seen.add((conn_cols[c][idx+1]-1, c))
                queue.append((conn_cols[c][idx+1]-1, c, d+1))

    return -1



if __name__ == '__main__':
    out = main()
    print(out)

