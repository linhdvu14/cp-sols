''' E1. Joking (Easy Version)
https://codeforces.com/contest/1746/problem/E1
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

def ask(x):
    output('?', len(x), *x)
    res = input().strip()
    return res == 'YES'

def guess(x):
    output(f'! {x}')
    res = input().strip()
    return res == ':)'


# divide into 4 partitions: A, B, C, D
# query A | B    A | C
# resp    Y        Y      -> not in D
#         N        N      -> not in A
#         Y        N      -> not in C
#         N        Y      -> not in B
# for n = 10^5, need 73 queries to narrow down to 3 cands
def reduce(cands):
    if len(cands) > 3:
        sz = len(cands) // 4
        a, b, c, d = cands[:sz], cands[sz:2*sz], cands[2*sz:3*sz], cands[3*sz:]
        rab = ask(a + b)
        rac = ask(a + c)
        if rab and rac: return a + b + c
        if not rab and not rac: return b + c + d
        if rab and not rac: return a + b + d 
        return a + c + d
    else:
        a, b, c = [cands[0]], [cands[1]], [cands[2]]
        ra, rb = ask(a), ask(b)
        if ra and rb: return a + b
        if not ra and rb: return b + c
        if ra and not rb: return a + c

        rb = ask(b)
        if not rb: return a + c

        ra = ask(a)
        if ra: return a + b
        return b + c


def main():
    N = int(input())
    
    cands = list(range(1, N + 1))
    while len(cands) > 2: cands = reduce(cands)
    
    assert guess(cands[0]) or (len(cands) == 2 and guess(cands[1]))


if __name__ == '__main__':
    main()