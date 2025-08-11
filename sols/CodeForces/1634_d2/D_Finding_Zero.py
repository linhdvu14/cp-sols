''' D. Finding Zero
https://codeforces.com/contest/1634/problem/D
'''

# to test: 
# pypy3 template.py
# or: python interactive_runner.py python local_testing_tool.py 0 -- python3 a.py

import functools
import os, sys
input = sys.stdin.readline  # io.BytesIO(os.read(0,os.fstat(0).st_size)).readline doesn't work
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

def ask(i, j, k):
    output(f'? {i} {j} {k}')
    res = int(input())
    assert res != -1
    return res


def find_extremes(a, b, c, d):
    '''return idx of mn and mx'''
    assert len(set([a, b, c, d])) == 4
    abc = ask(a, b, c)
    abd = ask(a, b, d)
    acd = ask(a, c, d)
    bcd = ask(b, c, d)
    ranges = sorted([(abc, 'abc'), (abd, 'abd'), (acd, 'acd'),  (bcd, 'bcd')], reverse=True)
    v1, k1 = ranges[0]
    v2, k2 = ranges[1]
    assert v1 == v2 and k1 > k2
    if k2 == 'abc' and k1 == 'abd': return a, b
    if k2 == 'abc' and k1 == 'acd': return a, c
    if k2 == 'abc' and k1 == 'bcd': return b, c
    if k2 == 'abd' and k1 == 'acd': return a, d
    if k2 == 'abd' and k1 == 'bcd': return b, d
    if k2 == 'acd' and k1 == 'bcd': return c, d


def solve():
    N = int(input())

    # track idx of min and max
    i, j = 1, 2
    for k in range(3, N, 2):
        i, j = find_extremes(i, j, k, k+1)

    if N % 2 == 1: 
        for k in range(1, N):
            if k != i and k != j:
                i, j = find_extremes(i, j, k, N)
                break

    output(f'! {i} {j}')



def main():
    T = int(input())
    for _ in range(T):
        solve()
    
 
if __name__ == '__main__':
    main()