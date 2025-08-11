''' Problem A2: Cottontail Climb (Part 2)
https://www.facebook.com/codingcompetitions/hacker-cup/2024/round-2/problems/A2
'''

import os, sys
input = sys.stdin.readline
output = sys.stdout.write

from inspect import currentframe, getframeinfo
from re import search
DEBUG = os.environ.get('debug') not in [None, '0']

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
from bisect import bisect_left, bisect_right

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


def gen_cands():
    seqs = []

    @bootstrap
    def dfs(cur):
        if len(cur) <= 8: 
            seqs.append(cur[:])
        if len(cur) < 8: 
            n = cur[-1]
            for i in range(n, 0, -1): 
                yield dfs(cur + [i])
        yield None

    for mid in range(1, 9):
        dfs([mid])

    L = [[] for _ in range(9)]
    R = [[] for _ in range(9)]
    for ds in seqs:
        l = r = 0
        for i, d in enumerate(ds):
            l += d * TEN[i]
            r = r * 10 + d
        L[len(ds)].append(l)
        R[len(ds)].append(r)

    cands = list(range(1, 10))
    for i in range(1, 9):
        for l in L[i]:
            for r in R[i]:
                for mid in range(max(l % 10, r // TEN[i - 1]) + 1, 10):
                    cands.append(l * TEN[i + 1] + mid * TEN[i] + r)
    
    cands.sort()
    return cands


TEN = [10**i for i in range(20)]
CANDS = gen_cands()

def solve(A, B, M):
    res = 0
    l = bisect_left(CANDS, A)
    r = bisect_right(CANDS, B) - 1

    if M == 1: return r - l + 1

    res = 0
    for i in range(l, r + 1):
        if CANDS[i] % M == 0:
            res += 1

    return res


def main():
    T = int(input())
    for t in range(T):
        A, B, M = list(map(int, input().split()))
        res = solve(A, B, M)
        print(f'Case #{t + 1}: {res}')


if __name__ == '__main__':
    main()

