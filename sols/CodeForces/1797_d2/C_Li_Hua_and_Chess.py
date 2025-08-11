''' C. Li Hua and Chess
https://codeforces.com/contest/1797/problem/C
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

def ask(r, c):
    output(f'? {r + 1} {c + 1}')
    res = int(input())
    return res


def guess(r, c):
    output(f'! {r + 1} {c + 1}')


def solve(R, C):
    x = ask(0, 0)
    y = ask(0, C - 1)
    
    if x + y == C - 1:
        z = ask(0, x)
        guess(z, x)
    elif x < y:
        guess(x, C - 1 - y)
    elif x > y:
        guess(y, x)
    else:   
        col = max(0, C - 1 - y)
        z = ask(x, col)
        guess(x, col + z)



def main():
    T = int(input())
    for _ in range(T):
        R, C = list(map(int, input().split()))
        solve(R, C)
    

if __name__ == '__main__':
    main()

