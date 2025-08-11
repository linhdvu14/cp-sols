''' Twisty Little Passages
https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a45fc0
'''

# to test: 
# pypy3 template.py
# or: python3 interactive_runner.py python3 local_testing_tool.py3 0 -- python3 a.py

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

# (1+e) multiplicative approximate algo
# https://people.csail.mit.edu/ronitt/COURSE/F20/Handouts/scribe2.pdf
# https://people.csail.mit.edu/ronitt/COURSE/F20/Handouts/scribe3.pdf
def solve1():
    import random
    from bisect import bisect_right
    from math import ceil, log, sqrt

    E = 1/6
    C = 1
    B = E/C

    def ask(s):
        output(s)
        res = input().strip()
        assert res != '-1'
        u, d = map(int, res.split())
        return u, d

    N, K = map(int, input().strip().split())

    # query all node degrees
    if N - 1 <= K:
        deg = 0
        u0, d0 = map(int, input().strip().split())
        deg += d0
        for u in range(N):
            if u+1 == u0: continue
            _, d = ask(f'T {u+1}')
            deg += d
        output(f'E {deg//2}')
        return
            
    # sample some nodes to query degrees
    # min t s.t. (1 + beta)^t >= n - 1
    T = ceil(log(N - 1, 1 + B)) + 1
    bounds = [(1 + B)**i for i in range(T)]

    S = random.sample(list(range(N)), K//2)
    bucket_cnt = [0] * T
    bucket_nei_cnt = [[0] * T for _ in range(T)]
    thres = sqrt(E/N) * len(S) / C / T

    _ = input()
    for u in S:
        _, deg = ask(f'T {u+1}')
        i = bisect_right(bounds, deg)
        bucket_cnt[i] += 1
        _, nei_deg = ask('W')
        j = bisect_right(bounds, nei_deg)
        bucket_nei_cnt[i][j] += 1

    P = [0] * T
    A = [0] * T
    for i in range(T):
        if bucket_cnt[i] >= thres:
            P[i] = bucket_cnt[i] / len(S)
            cnt = 0
            for j in range(T):
                if bucket_cnt[j] < thres:
                    cnt += bucket_nei_cnt[i][j]
            A[i] = cnt / bucket_cnt[i]
        else:
            P[i] = 0
    
    # avg degree
    res = 0
    for i in range(1, T):
        res += P[i] * (1 + A[i]) * (1 + B)**(i-1)
    output(f'E {int(res * N // 2)}')



# heuristics
# * T then W
# * T is unbiased avg
# * W are high-degree nodes -> add sum
def solve2():
    from random import randint
    
    def ask(s):
        output(s)
        res = input().strip()
        assert res != '-1'
        u, d = map(int, res.split())
        return u, d

    N, K = map(int, input().strip().split())

    # query all node degrees
    if N - 1 <= K:
        deg = 0
        u0, d0 = map(int, input().strip().split())
        deg += d0
        for u in range(N):
            if u+1 == u0: continue
            _, d = ask(f'T {u+1}')
            deg += d
        output(f'E {deg//2}')
        return
            
    _ = input()
    t_rooms = set()
    w_rooms = set()
    for _ in range(K//2):
        i = randint(0, N-1)
        r, d = ask(f'T {i+1}')
        assert r == i + 1
        t_rooms.add((r, d))
        r, d = ask('W')
        w_rooms.add((r, d))

    w_rooms -= t_rooms
    deg = sum(d for _, d in t_rooms) * N / len(t_rooms) + sum(d for _, d in w_rooms)
    output(f'E {int(deg/2)}')


# solve3: importance sampling
# * want to estimate avg degree E[d]
# * use K//2 samples on T, say degree A: p[d=A] = 1/N
# * use K//2 samples on W, say from degree A to degree B: q[d=B] = (1/N) * (1/A)


solve = solve2

def main():
    T = int(input())
    for _ in range(T):
        solve()
    
 
if __name__ == '__main__':
    main()