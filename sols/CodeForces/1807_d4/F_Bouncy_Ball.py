''' F. Bouncy Ball
https://codeforces.com/contest/1807/problem/F
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

DIR = {
    'DR': (1, 1),
    'DL': (1, -1),
    'UR': (-1, 1),
    'UL': (-1, -1),
}

def solve(R, C, r1, c1, r2, c2, d):
    def can_reach(r1, c1, r2, c2, dr, dc):
        nr = (r2 - r1) // dr 
        nc = (c2 - c1) // dc 
        return nr >= 0 and nc >= 0 and nr == nc

    def bounce(r1, c1, dr, dc):
        nr = R - 1 - r1 if dr == 1 else r1 
        nc = C - 1 - c1 if dc == 1 else c1 
        n = min(nr, nc)
        r2 = r1 + n * dr 
        c2 = c1 + n * dc
        if n == nr: dr = -dr 
        if n == nc: dc = -dc 
        return r2, c2, dr, dc

    r1 -= 1; c1 -= 1; r2 -= 1; c2 -= 1
    dr, dc = DIR[d]
    
    res = 0
    seen = set()
    while True:
        if can_reach(r1, c1, r2, c2, dr, dc): return res 
        r1, c1, dr, dc = bounce(r1, c1, dr, dc)
        if (r1, c1, dr, dc) in seen: return -1
        seen.add((r1, c1, dr, dc))
        res += 1



def main():
    T = int(input())
    for _ in range(T):
        ts = input().decode().strip().split()
        R, C, r1, c1, r2, c2 = list(map(int, ts[:-1]))
        d = ts[-1]
        res = solve(R, C, r1, c1, r2, c2, d)
        print(res)


if __name__ == '__main__':
    main()

