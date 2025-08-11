''' E. The Lakes
https://codeforces.com/contest/1829/problem/E
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

def solve(R, C, grid):
    res = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 0: continue
            cand = 0
            st = [(r, c)]
            while st:
                r1, c1 = st.pop()
                cand += grid[r1][c1]
                grid[r1][c1] = 0
                for r2, c2 in [(r1 + 1, c1), (r1 - 1, c1), (r1, c1 + 1), (r1, c1 - 1)]:
                    if not (0 <= r2 < R and 0 <= c2 < C): continue
                    if grid[r2][c2] == 0: continue
                    st.append((r2, c2))
            res = max(res, cand)

    return res


def main():
    T = int(input())
    for _ in range(T):
        R, C = list(map(int, input().split()))
        grid = [list(map(int, input().split())) for _ in range(R)]
        res = solve(R, C, grid)
        print(res)


if __name__ == '__main__':
    main()

