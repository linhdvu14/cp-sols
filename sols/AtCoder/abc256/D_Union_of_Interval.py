''' D - Union of Interval
https://atcoder.jp/contests/abc256/tasks/abc256_d
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
    segs = [list(map(int, input().split())) for _ in range(N)]
    segs.sort()

    res = []
    for l, r in segs:
        if not res or l > res[-1][-1]: res.append([l, r])
        else: res[-1][-1] = max(res[-1][-1], r)
    
    for l, r in res: print(l, r)



if __name__ == '__main__':
    main()

