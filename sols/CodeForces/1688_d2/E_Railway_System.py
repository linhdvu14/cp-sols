''' E. Railway System
https://codeforces.com/contest/1688/problem/E
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

def ask(q):
    s = ''.join(map(str, q))
    output(f'? {s}')
    res = int(input())
    return res


def main():
    N, M = list(map(int, input().split()))

    # M queries (0..010..0) to find lengths of all tracks
    L = [0] * M 
    q = [0] * M
    for i in range(M):
        q[i] = 1
        L[i] = ask(q)
        q[i] = 0

    # 1 query (1..1) to find max capacity with all tracks on + M-1 queries to rm tracks in descending length order
    # if removal decreases cap by len(i), i is in final min mst (disconnects 2 components)
    # if removal decreases cap by 0 or < len(i), i is not in final min mst
    # ALTERNATIVELY: M queries to add tracks in ascending length order
    # if adding increases cap by len(i), i is in final min sst (connects 2 components)
    # if adding increases cap by < len(i), i is not in final min set
    order = sorted(list(range(M)), key=lambda i: L[i])
    cap = res = 0
    q = [0] * M
    for i in order:
        q[i] = 1
        ncap = ask(q)
        if ncap - cap == L[i]: res += L[i]
        cap = ncap

    output(f'! {res}')


if __name__ == '__main__':
    main()