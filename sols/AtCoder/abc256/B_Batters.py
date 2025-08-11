''' B - Batters
https://atcoder.jp/contests/abc256/tasks/abc256_b
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
    A = list(map(int, input().split()))

    res = 0
    cur = [0] * 4
    for a in A:
        cur[0] = 1
        nxt = [0] * 4
        for i in range(4):
            if not cur[i]: continue
            if i + a >= 4: res += 1
            else: nxt[i + a] = 1
        cur = nxt
    
    return res


if __name__ == '__main__':
    out = main()
    print(out)

