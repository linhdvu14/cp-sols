''' D. Bit Guessing Game
https://codeforces.com/contest/1780/problem/D
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
    output(f'- {x}')
    res = int(input())
    assert res != -1
    return res


def solve():
    cnt = int(input())

    res = sub = 0
    for b in range(30):
        ncnt = ask((1 << b) - sub)
        if ncnt < cnt: 
            res |= 1 << b
            cnt = ncnt
            sub = 0
        else:
            sub = 1 << b
        if not cnt: break

    output(f'! {res}')


def main():
    T = int(input())
    for _ in range(T):
        solve()
    
 
if __name__ == '__main__':
    main()
