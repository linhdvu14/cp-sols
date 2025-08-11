''' C - Rotation
https://atcoder.jp/contests/abc258/tasks/abc258_c
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') not in [None, '0']

if DEBUG:
    from inspect import currentframe, getframeinfo
    from re import search

def debug(*args):
    if not DEBUG: return
    frame = currentframe().f_back
    s = getframeinfo(frame).code_context[0]
    r = search(r"\((.*)\)", s).group(1)
    vnames = r.split(', ')
    var_and_vals = [f'{var}={val}' for var, val in zip(vnames, args)]
    prefix = f'{currentframe().f_back.f_lineno:02d}: '
    print(f'{prefix}{", ".join(var_and_vals)}')


INF = float('inf')

# -----------------------------------------

def main():
    N, Q = list(map(int, input().split()))
    S = input().decode().strip()
    
    i = 0
    res = []
    for _ in range(Q):
        t, x = list(map(int, input().split()))
        if t == 1: i += N - x
        else: res.append(S[(i + x - 1) % N])
    
    print(*res, sep='\n')


if __name__ == '__main__':
    main()

