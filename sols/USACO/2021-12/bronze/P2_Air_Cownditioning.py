''' Problem 2. Air Cownditioning 
http://www.usaco.org/index.php?page=viewproblem2&cpid=1156
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

def solve(N, A, B):
    def solve_block(D):
        if not D: return 0

        # reduce to spikes
        D = [0] + [abs(d) for d in D]
        D = [d for i, d in enumerate(D) if i==0 or d != D[i-1]]
        D = [d for i, d in enumerate(D) if i==0 or i==len(D)-1 or (d-D[i-1])*(d-D[i+1])>0]

        # add hills
        res = 0
        for i in range(1, len(D), 2):
            res += D[i] - D[i-1]
        return res

    res = 0
    D = []
    for a, b in zip(A, B):
        d = b-a
        if d == 0 or (D and d*D[-1] < 0):
            res += solve_block(D)
            D = []
        if d != 0: D.append(d)
    res += solve_block(D)

    return res


def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))    
    out = solve(N, A, B)
    output(f'{out}\n')


if __name__ == '__main__':
    main()

