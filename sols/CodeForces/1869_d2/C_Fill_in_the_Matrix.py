''' C. Fill in the Matrix
https://codeforces.com/contest/1869/problem/C
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

def solve(R, C):
    if C == 1: return 0, [[0]] * R

    m = min(R + 1, C)
    grid = []
    for i in range(R):
        row = list(range(C))
        if i + 1 < m: row[:m] = row[:m][i:] + row[:m][:i]
        grid.append(row)

    return m, grid


def main():
    T = int(input())
    for _ in range(T):
        R, C = list(map(int, input().split()))
        m, grid = solve(R, C)
        print(m)
        for r in grid: print(*r)

if __name__ == '__main__':
    main()
