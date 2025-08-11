''' B - Practical Computing
https://atcoder.jp/contests/abc254/tasks/abc254_b
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
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
    N = int(input())
    res = []
    for i in range(N):
        A = []
        for j in range(i+1):
            if j == 0 or j == i: A.append(1)
            else: A.append(res[i-1][j-1] + res[i-1][j])
        res.append(A)    
    for A in res: print(*A)


if __name__ == '__main__':
    main()

