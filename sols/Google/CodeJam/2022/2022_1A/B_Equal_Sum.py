''' Equal Sum 
https://codingcompetitions.withgoogle.com/codejam/round/0000000000877ba5/0000000000aa8fc1
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
    sys.stderr.write(f'{prefix}{", ".join(var_and_vals)}' + '\n')


INF = float('inf')

# -----------------------------------------

BITS = 30
LEN = 100

A1 = [1 << i for i in range(BITS)]
A2 = []
for a in range(1, 10**9):
    if len(A1) + len(A2) == LEN: break
    if a not in A1: A2.append(a)


def ask(nums):
    output(*nums)
    res = input().strip()
    assert res != '-1'
    return list(map(int, res.split()))


def solve():
    N = int(input())
    assert N == LEN

    B = ask(A1 + A2)
    res = []
    bal = 0

    # distribute B + A2; |bal| <= 10**9
    for x in B + A2:
        if bal < 0:
            bal += x
            res.append(x)
        else:
            bal -= x

    # distribute A1; |bal| decreases to 0
    for i in range(BITS-1, -1, -1):
        if bal < 0:
            bal += 1 << i
            res.append(1 << i)
        else:
            bal -= 1 << i

    assert bal == 0
    output(*res)


def main():
    T = int(input())
    for _ in range(T):
        solve()
    
 
if __name__ == '__main__':
    main()