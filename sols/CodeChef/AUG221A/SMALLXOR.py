''' XOR with smallest element
https://www.codechef.com/AUG221A/problems/SMALLXOR
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

# simulate until a number decreases or doesn't change
# <= N steps

from heapq import heappush, heappop, heapify

def solve(N, X, Y, A):
    heapify(A)

    while Y:
        Y -= 1
        a = heappop(A)
        b = a ^ X
        if b <= a: 
            Y %= 2
            if Y: heappush(A, a)
            else: heappush(A, b)
            break 
        heappush(A, b)
    
    res = []
    while A: res.append(heappop(A))
    return res
        

def main():
    T = int(input())
    for _ in range(T):
        N, X, Y = list(map(int, input().split()))
        A = list(map(int, input().split()))
        out = solve(N, X, Y, A)
        print(*out)


if __name__ == '__main__':
    main()

