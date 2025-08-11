''' Min Manhattan Distance
https://www.codechef.com/DEC21B/problems/MINMANH
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') is not None

if DEBUG:
    from varname.core import argname
    from inspect import currentframe

def debug(var, *more_vars):
    if not DEBUG: return
    var_names = argname('var', '*more_vars', func=debug)
    values = (var, *more_vars)
    name_and_values = [f'{var_name}={value}'  for var_name, value in zip(var_names, values)]
    prefix = f'{currentframe().f_back.f_lineno:02d}: '
    print(f'{prefix}{", ".join(name_and_values)}')


INF = float('inf')

# -----------------------------------------


class BIT:
    def __init__(self, N):
        self.N = N
        self.tree = [-INF]*(N+1)

    def query(self, i):
        '''max first i numbers A[1..i]'''
        s = -INF
        while i > 0:
            s = max(s, self.tree[i])
            i -= i & (-i)  # 110 -> 100
        return s

    def update(self, i, val):
        '''update A[i] = max(A[i], val) (1-based)'''
        while i <= self.N:
            self.tree[i] = max(self.tree[i], val)
            i += i & (-i)  # 101 -> 110


# https://youtu.be/BgmyTNw7f08
def solve(N, M, S, T):
    res = [INF]*M

    points = [(x, y, i) for i, (x, y) in enumerate(T)] + [(x, y, -1) for x, y in S]

    # for each query point (x, y) in T, find the closest point (sx, sy) in S in its bottom left quadrant 
    # then abs(x - sx) + abs(y - sy) = (x + y) - (sx + sy) 
    def solve_quadrant(xm, ym):
        nonlocal points
        points = [(x*xm, y*ym, i) for x, y, i in points]
        points.sort(key=lambda tup: (tup[1], tup[0], tup[2]))

        # compress x coords
        idx_map = sorted(list(set([x for x, _, _ in points])))
        idx_map = {x: i+1 for i, x in enumerate(idx_map)}
        
        # add S points to BIT from lowest y to highest y
        # for each query point (x, y), find max (sx + sy) among all added points with sx <= x
        bit = BIT(len(idx_map))
        for x, y, qi in points:
            if qi == -1:
                bit.update(idx_map[x], x+y)
            else:
                res[qi] = min(res[qi], x + y - bit.query(idx_map[x]))
            
    # solve for all 4 quadrants
    for xm, ym in [(1, 1), (1, -1), (-1, 1), (1, -1)]:
        solve_quadrant(xm, ym)

    for r in res: print(r)
    

def main():
    N, M = list(map(int, input().split()))
    S = [tuple(map(int, input().split())) for _ in range(N)]
    T = [tuple(map(int, input().split())) for _ in range(M)]
    solve(N, M, S, T)


if __name__ == '__main__':
    main()

