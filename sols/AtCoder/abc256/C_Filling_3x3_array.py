''' C - Filling 3x3 array
https://atcoder.jp/contests/abc256/tasks/abc256_c
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
    h1, h2, h3, w1, w2, w3 = list(map(int, input().split()))

    def split(n):
        res = []
        for a in range(1, n):
            for b in range(1, n):
                c = n - a - b
                if c > 0: res.append((a, b, c))
        return res
    
    rows1 = split(h1)
    rows2 = split(h2)

    res = 0
    for a1, a2, a3 in rows1:
        for b1, b2, b3 in rows2:
            c1 = w1 - a1 - b1
            c2 = w2 - a2 - b2
            c3 = w3 - a3 - b3
            if min(c1, c2, c3) < 1: continue
            if c1 + c2 + c3 != h3: continue
            res += 1
    
    print(res)




if __name__ == '__main__':
    main()

