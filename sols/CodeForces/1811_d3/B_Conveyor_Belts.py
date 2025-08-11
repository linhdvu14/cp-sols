''' B. Conveyor Belts
https://codeforces.com/contest/1811/problem/B
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

def solve(N, x1, y1, x2, y2):
    a = min(x1, N + 1 - x1, y1, N + 1 - y1)
    b = min(x2, N + 1 - x2, y2, N + 1 - y2)
    return abs(a - b)


def main():
    T = int(input())
    for _ in range(T):
        N, x1, y1, x2, y2 = list(map(int, input().split()))
        res = solve(N, x1, y1, x2, y2)
        print(res)


if __name__ == '__main__':
    main()

