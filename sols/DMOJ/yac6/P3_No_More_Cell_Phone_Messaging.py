''' Yet Another Contest 6 P3 - No More Cell Phone Messaging
https://dmoj.ca/problem/yac6p3
'''

import functools
import os, sys
input = sys.stdin.readline  # strip() if str; io.BytesIO(os.read(0,os.fstat(0).st_size)).readline doesn't work
output = functools.partial(print, flush=True)

DEBUG = os.environ.get('debug') not in [None, '0']

def debug(*args):   
    if not DEBUG: return
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

def ask(x, y):
    output(f'? {x + 1} {y + 1}')
    res = int(input())
    assert res != -1
    return res


def main():
    n, m = list(map(int, input().split()))

    d1 = ask(0, 0)          # x + y = d1
    d2 = ask(n - 1, m - 1)  # x + y = m + n - 2 - d2
    d3 = ask(n - 1, 0)      # x - y = n - 1 - d3
    d4 = ask(0, m - 1)      # x - y = -m + 1 + d4

    # find intersections
    p13 = p14 = p23 = p24 = None 
    if (d1 + n - 1 - d3) % 2 == 0:
        x13 = (d1 + n - 1 - d3) // 2
        y13 = (d1 - n + 1 + d3) // 2
        if 0 <= x13 <= n - 1 and 0 <= y13 <= m - 1: p13 = (x13, y13)
    if (d1 - m + 1 + d4) % 2 == 0:
        x14 = (d1 - m + 1 + d4) // 2
        y14 = (d1 + m - 1 - d4) // 2
        if 0 <= x14 <= n - 1 and 0 <= y14 <= m - 1: p14 = (x14, y14)
    if (m + n - 2 - d2 + n - 1 - d3) % 2 == 0:
        x23 = (m + n - 2 - d2 + n - 1 - d3) // 2
        y23 = (m + n - 2 - d2 - n + 1 + d3) // 2
        if 0 <= x23 <= n - 1 and 0 <= y23 <= m - 1: p23 = (x23, y23)
    if (m + n - 2 - d2 - m + 1 + d4) % 2 == 0:
        x24 = (m + n - 2 - d2 - m + 1 + d4) // 2
        y24 = (m + n - 2 - d2 + m - 1 - d4) // 2
        if 0 <= x24 <= n - 1 and 0 <= y24 <= m - 1: p24 = (x24, y24)
    
    cands = list(set(p for p in [p13, p14, p23, p24] if p))
    assert len(cands) in [2, 3, 4]
    
    if len(cands) == 2:
        a, b = cands[0]
        c, d = cands[1]
    elif len(cands) == 3:
        if not p13 or not p24: 
            a, b = p14 
            c, d = p23
        else:
            a, b = p13 
            c, d = p24
    else:
        d = ask(*p13)
        if d == 0:
            a, b = p13 
            c, d = p24 
        else:
            a, b = p14
            c, d = p23
        
    output(f'! {a + 1} {b + 1} {c + 1} {d + 1}')



 
if __name__ == '__main__':
    main()