''' D. Sum Graph
https://codeforces.com/contest/1816/problem/D
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

def ask1(x):
    output(f'+ {x}')
    res = int(input())
    assert res != -2
    return res


def ask2(i, j):
    output(f'? {i} {j}')
    res = int(input())
    assert res != -2
    return res


def guess(p1, p2):
    output('!', *p1, *p2)
    res = int(input())
    assert res != -2


def solve(N):
    # create line tree: N, 1, N - 1, 2, N - 2, 3, N - 3, ... (N + 1) // 2
    ask1(N + 1)
    ask1(N)

    line = [N]
    for i in range((N - 1) // 2):
        line.append(i + 1)
        line.append(N - i - 1)
    if N % 2 == 0: line.append(N // 2)
        
    # find one endpoint
    mx = (0, 0)
    for i in range(2, N + 1):
        d = ask2(1, i)
        mx = max(mx, (d, i))
    _, end = mx

    dists = [(0, end)]
    for i in range(1, N + 1):
        if i == end: continue
        d = ask2(end, i)
        dists.append((d, i))
    dists.sort()

    # end is either N or (N + 1) // 2
    res1 = [-1] * N
    res2 = [-1] * N
    for i, (_, idx) in enumerate(dists):
        res1[idx - 1] = line[i]
        res2[idx - 1] = line[-1 - i]

    guess(res1, res2)


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        solve(N)
    

if __name__ == '__main__':
    main()

