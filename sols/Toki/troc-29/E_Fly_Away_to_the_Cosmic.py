''' E. Fly Away to the Cosmic
https://tlx.toki.id/contests/troc-29/problems/E
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

# greedy solution: max(A) + 1
# if both groups have >= 2 elements say (a, b) and (c, d), then gcd(a, b) + gcd(c, d) <= max(a, b, c, d)
# so 1 group must have 1 element

from math import gcd

def main():
    N = int(input())
    A = list(map(int, input().split()))

    left = [0] * N 
    left[1] = A[0]
    for i in range(2, N): left[i] = gcd(left[i - 1], A[i - 1])

    right = [0] * N
    right[N - 2] = A[N - 1]
    for i in range(N - 3, -1, -1): right[i] = gcd(right[i + 1], A[i + 1])

    res = 0
    for i, a in enumerate(A):
        res = max(res, a + gcd(left[i], right[i]))
    
    print(res)


if __name__ == '__main__':
    main()

