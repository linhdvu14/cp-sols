''' D. Accommodation
https://codeforces.com/contest/1804/problem/D 
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

def solve(N, M, grid):
    mn = mx = 0
    for row in grid:
        tot = row.count('1')
        
        # to min windows, max num 2br spanning 11
        two = i = 0
        while i < M:
            if i + 1 < M and row[i] == row[i + 1] == '1':
                two += 1
                i += 2
            else:
                i += 1
        mn += tot - min(two, M // 4) 

        # to max windows, min num 2br spanning 11
        two = i = 0
        while i < M:
            if i + 1 < M and (row[i] == '0' or row[i + 1] == '0'):
                two += 1
                i += 2
            else:
                i += 1
        mx += tot - (M // 4 - min(two, M // 4))

    return mn, mx


def main():
    N, M = list(map(int, input().split()))
    grid = [input().decode().strip() for _ in range(N)]
    res = solve(N, M, grid)
    print(*res)


if __name__ == '__main__':
    main()

