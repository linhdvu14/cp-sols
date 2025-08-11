''' A. Walking Master
https://codeforces.com/contest/1806/problem/A
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

def solve(x1, y1, x2, y2):
    if y2 < y1: return -1
    res = y2 - y1
    x1 += y2 - y1 
    if x1 < x2: return -1
    res += x1 - x2
    return res


def main():
    T = int(input())
    for _ in range(T):
        x1, y1, x2, y2 = list(map(int, input().split()))
        res = solve(x1, y1, x2, y2)
        print(res)


if __name__ == '__main__':
    main()

