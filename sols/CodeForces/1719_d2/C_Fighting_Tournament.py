''' C. Fighting Tournament
https://codeforces.com/contest/1719/problem/C
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def debug(*args):   
    if os.environ.get('debug') in [None, '0']: return
    from inspect import currentframe, getframeinfo
    from re import search
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
    def __contains__(self, k): return super().__contains__(k^self.rand)
    def __repr__(self): return str({k: v for k, v in self.items()})
    def get(self, k, default=None): return super().get(k^self.rand, default)
    def keys(self): return [k^self.rand for k in super().keys()]
    def items(self): return [(k^self.rand, v) for k, v in super().items()]

INF = float('inf')

# -----------------------------------------

from collections import deque
from bisect import bisect_right

def solve(N, Q, A, queries):
    wins = [[] for _ in range(N+1)]
    B = deque(A[:])
    r = 0
    while B[0] != N: 
        a, b = B.popleft(), B.popleft()
        a, b = max(a, b), min(a, b)
        B.appendleft(a)
        B.append(b)
        if a < N: 
            r += 1
            wins[a].append(r) 

    res = []
    for i, k in queries:
        i -= 1
        if A[i] == N: res.append(max(0, k - r))
        else: res.append(bisect_right(wins[A[i]], k))

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, Q = list(map(int, input().split()))
        A = list(map(int, input().split()))
        queries = [list(map(int, input().split())) for _ in range(Q)]
        out = solve(N, Q, A, queries)
        print(*out, sep='\n')


if __name__ == '__main__':
    main()

