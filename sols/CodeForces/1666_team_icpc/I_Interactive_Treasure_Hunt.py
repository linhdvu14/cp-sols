''' I. Interactive Treasure Hunt
https://codeforces.com/contest/1666/problem/I
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

def scan(r, c):
    output(f'SCAN {r+1} {c+1}')
    res = int(input())
    return res

def dig(r, c):
    output(f'DIG {r+1} {c+1}')
    res = int(input())
    return res


def solve():
    R, C = list(map(int, input().split()))

    ul = scan(0, 0)   # r1 + r2 + c1 + c2
    ur = scan(0, C-1) # r1 + r2 + 2*(C-1) - c1 - c2
    sum_r = (ul + ur - 2*(C-1)) // 2  # r1 + r2
    sum_c = (ul - ur + 2*(C-1)) // 2  # c1 + c2
    
    ml = scan(sum_r // 2, 0)  # abs(r1 - r2) + c1 + c2
    mr = scan(0, sum_c // 2)  # r1 + r2 + abs(c1 - c2)
    diff_r = ml - sum_c
    diff_c = mr - sum_r

    r1, r2 = (sum_r + diff_r) // 2, (sum_r - diff_r) // 2
    c1, c2 = (sum_c + diff_c) // 2, (sum_c - diff_c) // 2

    f = dig(r1, c1)
    if f == 1:
        f = dig(r2, c2)
        assert f == 1
    else:
        f = dig(r1, c2)
        assert f == 1
        f = dig(r2, c1)
        assert f == 1


def main():
    T = int(input())
    for _ in range(T):
        solve()
    
 
if __name__ == '__main__':
    main()