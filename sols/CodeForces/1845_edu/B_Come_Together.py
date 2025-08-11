''' B. Come Together
https://codeforces.com/contest/1845/problem/B
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

def solve(xa, ya, xb, yb, xc, yc):
    dxb, dyb = xb - xa, yb - ya
    dxc, dyc = xc - xa, yc - ya 
    res = 1 + (min(abs(dxb), abs(dxc)) if dxb * dxc >= 0 else 0) + \
        (min(abs(dyb), abs(dyc)) if dyb * dyc >= 0 else 0)
    return res


def main():
    T = int(input())
    for _ in range(T):
        xa, ya = list(map(int, input().split()))
        xb, yb = list(map(int, input().split()))
        xc, yc = list(map(int, input().split()))
        res = solve(xa, ya, xb, yb, xc, yc)
        print(res)


if __name__ == '__main__':
    main()

