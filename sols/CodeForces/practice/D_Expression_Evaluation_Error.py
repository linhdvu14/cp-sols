''' D. Expression Evaluation Error
https://codeforces.com/contest/1567/problem/D
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

# greedily max sum of digits at each pos over all nums, from highest to lowest pos

def solve(S, N):
    res = [0] * N
    ten = 10**9
    pos = 0  # idx of first zero ele in res; N - x is num nonzero eles left
    
    while ten:
        # greedily use max number of ten powers s.t. enough to make res nonzero
        for x in range(N - pos, -1, -1):  
            if S - ten * x + x >= N - pos:
                for i in range(pos, pos + x): res[i] += ten 
                S -= x * ten
                pos += x
                break 
        ten //= 10

    res[0] += S
    return res


def main():
    T = int(input())
    for _ in range(T):
        S, N = list(map(int, input().split()))
        out = solve(S, N)
        print(*out)


if __name__ == '__main__':
    main()

