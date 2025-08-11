''' A. Li Hua and Maze
https://codeforces.com/contest/1797/problem/A
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

def solve(R, C, x1, y1, x2, y2):
    corners = [(1, 1), (1, C), (R, 1), (R, C)]
    if (x1, y1) in corners or (x2, y2) in corners: return 2
    if x1 in [1, R] or x2 in [1, R] or y1 in [1, C] or y2 in [1, C]: return 3
    return 4


def main():
    T = int(input())
    for _ in range(T):
        R, C = list(map(int, input().split()))
        x1, y1, x2, y2 = list(map(int, input().split()))
        res = solve(R, C, x1, y1, x2, y2)
        print(res)


if __name__ == '__main__':
    main()

