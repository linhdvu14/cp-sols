''' Problem C: Fall in Line
https://www.facebook.com/codingcompetitions/hacker-cup/2024/practice-round/problems/C
'''

import os, sys
input = sys.stdin.readline
output = sys.stdout.write

from inspect import currentframe, getframeinfo
from re import search
DEBUG = os.environ.get('debug') not in [None, '0']
DEBUG_CASE = int(os.environ.get('case', 0))

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
import random
random.seed(123)
from math import gcd

def get_line_2d(p, q):
    ''' return a, b, c s.t. ax + by + c = 0
    y-y1 = (y2-y1)/(x2-x1) * (x-x1)
    '''
    if p == q: return (0, 0, 0)
    if p > q: p, q = q, p
    a, b, c = q[1] - p[1], p[0] - q[0], p[1] * q[0] - p[0] * q[1]
    g = gcd(gcd(a, b), c)
    return a // g, b // g, c // g


# case 1: n < 1e4
# case 2: n >= 1e4, colinear count >= n/2
# case 3: n >= 1e4, colinear count < n/2
def solve(N, P):
    if N < 10000:
        cnt = {}
        for i, p in enumerate(P):
            for j in range(i):
                coord = get_line_2d(p, P[j])
                cnt[coord] = cnt.get(coord, 0) + 1
        mx = max(cnt.values())
        sq = int((mx * 2)**0.5)
        for x in range(sq - 1, sq + 2):
            if x * (x - 1) // 2 == mx:
                return N - x
    
    for _ in range(100):
        i = j = random.randint(0, N - 1)
        while j == i: j = random.randint(0, N - 1)
        a, b, c = get_line_2d(P[i], P[j])
        x = sum(1 for x, y in P if a * x + b * y + c == 0)
        if x >= N / 2:           
            return N - x
    
    return N - 2


def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        P = [list(map(int, input().split())) for _ in range(N)]
        if DEBUG and DEBUG_CASE and t != DEBUG_CASE: continue
        res = solve(N, P)
        print(f'Case #{t + 1}: {res}')


if __name__ == '__main__':
    main()

