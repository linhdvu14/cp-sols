''' B. Points on Plane
https://codeforces.com/contest/1809/problem/B
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

# rotate 45 deg into square; fit (d + 1)^2 points
def solve(N):
    if N == 1: return 0
    d = int(N ** 0.5)
    while d * d < N: d += 1
    return d - 1


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        res = solve(N)
        print(res)



if __name__ == '__main__':
    main()

