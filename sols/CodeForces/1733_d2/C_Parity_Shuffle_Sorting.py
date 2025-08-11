''' C. Parity Shuffle Sorting
https://codeforces.com/contest/1733/problem/C
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

def solve_1(N, A):
    last = [-1] * 2
    for i, a in enumerate(A): last[a % 2] = i

    res = []
    p = A[0] % 2
    if last[p] != 0: res.append((1, last[p] + 1))

    for i in range(1, N - 1):
        a = A[i]
        if a % 2 != p: res.append((1, i + 1))
        elif a % 2 == p and i != last[a % 2]: res.append((i + 1, last[p] + 1))

    return res


def solve_2(N, A):
    if N == 1: return []

    res = [(1, N)]
    if (A[0] + A[N - 1]) & 1: A[N - 1] = A[0]
    else: A[0] = A[N - 1]

    for i in range(1, N - 1):
        if (A[i] + A[0]) & 1: res.append((1, i + 1))
        else: res.append((i + 1, N))
    
    return res


solve = solve_2


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        res = solve(N, A)
        print(len(res))
        for t in res: print(*t)


if __name__ == '__main__':
    main()

