''' D. GCD Guess
https://codeforces.com/contest/1665/problem/D
'''

# to test: 
# pypy3 template.py
# or: python3 interactive_runner.py python3 local_testing_tool.py 0 -- python3 a.py

import functools
import os, sys
input = sys.stdin.readline  # strip() if str; io.BytesIO(os.read(0,os.fstat(0).st_size)).readline doesn't work
output = functools.partial(print, flush=True)

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
X = 1000000000

def answer(a, b): 
    from math import gcd
    return gcd(X + a, X + b)


def ask(a, b):
    assert 1 <= a <= 2 * 10**9 and 1 <= b <= 2 * 10**9 and a != b, f'a={a} b={b}'
    if DEBUG: return answer(a, b)
    output(f'? {a} {b}')
    res = int(input())
    assert res != -1
    return res


# progressively determine r[i] = x % 2^i for i=0..30
# then 
# * r[i] = last i bits of x
# * r[0] = 0; r[30] = x
# * x - r[i] has >= i last 0 bits
# given r[i], the i-th bit is 0 iff gcd(x - r[i], 1 << (i+1)) == 1 << (i+1)
# i.e. the i-th bit is 1 iff gcd(x - r[i] + (1 << i), 1 << (i+1)) == 1 << (i+1)

def solve():
    r = 0
    for i in range(30):
        p = 1 << i
        q = 1 << (i+1)
        g = ask(p - r, p + q - r)
        if g == q: r |= p
    if DEBUG: assert r == X, f'exp={X} got={r}'
    output(f'! {r}')


def main():
    T = int(input())
    for _ in range(T):
        solve()

 
if __name__ == '__main__':
    main()