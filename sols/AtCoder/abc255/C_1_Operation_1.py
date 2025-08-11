''' C - ±1 Operation 1
https://atcoder.jp/contests/abc255/tasks/abc255_c
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

def solve(x, a, d, n):
    if (x - a) * d <= 0: return abs(x - a)
    
    t, r = divmod(x - a, d)
    res = abs(a + (n-1)*d - x)
    if t <= n-1: res = min(res, abs(r))
    if t < n-1: res = min(res, abs(d-r))

    return res


def main():
    x, a, d, n = list(map(int, input().split()))
    out = solve(x, a, d, n)
    print(out)


if __name__ == '__main__':
    main()
