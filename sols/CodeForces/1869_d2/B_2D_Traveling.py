''' B. 2D Traveling
https://codeforces.com/contest/1869/problem/B
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

def solve(N, K, a, b, points):
    x1, y1 = points[a - 1]
    x2, y2 = points[b - 1]

    mn1 = mn2 = INF
    for i in range(K):
        x, y = points[i]
        mn1 = min(mn1, abs(x1 - x) + abs(y1 - y))
        mn2 = min(mn2, abs(x2 - x) + abs(y2 - y))
    
    res = min(mn1 + mn2, abs(x1 - x2) + abs(y1 - y2))
    return res


def main():
    T = int(input())
    for _ in range(T):
        N, K, a, b = list(map(int, input().split()))
        points = [list(map(int, input().split())) for _ in range(N)]
        res = solve(N, K, a, b, points)
        print(res)


if __name__ == '__main__':
    main()

