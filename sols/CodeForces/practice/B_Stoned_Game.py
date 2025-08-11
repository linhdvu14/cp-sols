''' B. Stoned Game
https://codeforces.com/contest/1396/problem/B
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

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


class IntKeyDict(dict):
    from random import randrange
    rand = randrange(1 << 62)
    def __setitem__(self, k, v): super().__setitem__(k^self.rand, v)
    def __getitem__(self, k): return super().__getitem__(k^self.rand)


INF = float('inf')

# -----------------------------------------

# optimal for each player to pick pile with most remaining stones available to them
from heapq import heappush, heappop

def solve_1(N, A):
    h = []
    for a in A: heappush(h, -a)

    turn = save = 0
    while h:
        turn ^= 1
        a = -heappop(h)
        if save: heappush(h, save)
        save = -a + 1

    return 'T' if turn else 'HL'


# Alice wins if there's a pile with > sum(A) // 2 stones, or sum(A) odd
# otherwise, can assign stones 0..A[0]-1 to pile 0, A[0]..A[0]+A[1]-1 to pile 1, ...
# and match stone (i, i + S//2)
def solve_2(N, A):
    S = sum(A)
    if any(a > S//2 for a in A) or S % 2: return 'T'
    return 'HL'


solve = solve_2

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        out = solve(N, A)
        print(out)


if __name__ == '__main__':
    main()

