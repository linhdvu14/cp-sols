''' C. Almost All Multiples
https://codeforces.com/contest/1758/problem/C
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

def factorize(n):
    small, large = [], []
    for i in range(1, int(n**0.5) + 1, 2 if n & 1 else 1):
        if n % i == 0:
            small.append(i)
            large.append(n // i)
    if small[-1] == large[-1]: large.pop()
    return small + large[::-1]


def solve(N, x):
    if N % x: return [-1]

    A = list(range(N + 1))
    A[1], A[N] = A[N], A[1]
    
    if x != N: 
        A[1], A[x] = A[x], A[1]
        divs = factorize(N)
        for d in divs:
            if d <= x or d == N: continue
            if N % d == 0 and A[d] % x == 0: A[x], A[d], x = A[d], A[x], d
    
    return A[1:]


def main():
    T = int(input())
    for _ in range(T):
        N, x = list(map(int, input().split()))
        res = solve(N, x)
        print(*res)


from itertools import permutations
def truth(N, X):
    res = None
    for A in permutations(list(range(1, N + 1))):
        if not (A[0] == X and A[-1] == 1): continue
        if not all(A[i] % (i + 1) == 0 for i in range(N - 1)): continue
        if not res or res < A: res = A 
    return list(res) if res else [-1]


def gen():
    import random
    random.seed(123)

    for _ in range(100):
        N = random.randint(2, 15)
        X = random.randint(2, N)
        exp = truth(N, X)
        got = solve(N, X)
        if exp != got:
            print(N, X)
            print(f'exp={exp}')
            print(f'got={got}')
            exit(1)
    print('tests passed')


if __name__ == '__main__':
    main()
    # gen()

