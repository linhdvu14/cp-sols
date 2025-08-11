''' C. The Very Beautiful Blanket
https://codeforces.com/contest/1802/problem/C
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
    res = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            res[r][c] = (r << 10) | c

    return R * C, res


def main():
    T = int(input())
    for _ in range(T):
        R, C = list(map(int, input().split()))
        a, b = solve(R, C)
        print(a)
        for t in b: print(*t)


if __name__ == '__main__':
    main()

