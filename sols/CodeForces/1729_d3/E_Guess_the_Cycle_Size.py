''' E. Guess the Cycle Size
https://codeforces.com/contest/1729/problem/E
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

def ask(a, b):
    output(f'? {a} {b}')
    res = int(input())
    assert res != 0
    return res


def main():
    for b in range(2, 27):
        d1 = ask(1, b)
        d2 = ask(b, 1)
        if d1 == -1:
            output(f'! {b-1}')
            return
        if d1 != d2:
            output(f'! {d1+d2}')
            return

    assert False
 

if __name__ == '__main__':
    main()