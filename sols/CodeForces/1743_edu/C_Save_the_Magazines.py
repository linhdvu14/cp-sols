''' C. Save the Magazines
https://codeforces.com/contest/1743/problem/C
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

def solve_1(N, B, A):
    res = sum(A)
    i = 0
    while i < N and B[i] == 1: i += 1
    while i < N:
        mn = A[i]
        i += 1
        while i < N and B[i] == 1:
            mn = min(mn, A[i])
            i += 1
        res -= mn

    return res


def solve_2(N, B, A):
    j = -1
    for i, b in enumerate(B):
        if b == 0: 
            j = i
        elif j >= 0 and A[j] > A[i]: 
            B[i], B[j] = B[j], B[i]
            j = i

    return sum(a for a, b in zip(A, B) if b == 1)


solve = solve_2

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        B = list(map(int, input().decode().strip()))
        A = list(map(int, input().split()))
        res = solve(N, B, A)
        print(res)


if __name__ == '__main__':
    main()

