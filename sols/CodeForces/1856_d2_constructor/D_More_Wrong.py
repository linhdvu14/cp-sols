''' D. More Wrong
https://codeforces.com/contest/1856/problem/D
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
from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack: return f(*args, **kwargs)
        to = f(*args, **kwargs)
        while True:
            if type(to) is GeneratorType:
                stack.append(to)
                to = next(to)
            else:
                stack.pop()
                if not stack: break
                to = stack[-1].send(to)
        return to
    return wrappedfunc


def ask(l, r):
    if l >= r: return 0
    output(f'? {l + 1} {r + 1}')
    res = int(input())
    assert res != -1
    return res

def answer(x):
    output(f'! {x + 1}')

# 2 * N^2 * (1 + 1/2 + 1/2^2 + 1/2^3 + ...) = 4 * N^2
def solve(N):
    @bootstrap
    def _solve(l, r):
        if l == r: yield l
        if l + 1 == r: yield l if ask(l, r) else r
        m = (l + r) // 2
        i1 = yield _solve(l, m)
        i2 = yield _solve(m + 1, r)
        yield i2 if ask(i1, i2) == ask(i1, i2 - 1) else i1

    i = _solve(0, N - 1)
    answer(i)


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        solve(N)

if __name__ == '__main__':
    main()
