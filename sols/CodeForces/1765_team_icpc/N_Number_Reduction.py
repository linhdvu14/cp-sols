''' N. Number Reduction
https://codeforces.com/contest/1765/problem/N
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

from bisect import bisect_left

def solve(A, K):
    pos = [[] for _ in range(10)]
    for i, d in enumerate(A): pos[d].append(i)

    res = []
    start = 0
    while len(A) - start > K:
        for d in range(10):
            if d == 0 and not res: continue
            idx = bisect_left(pos[d], start)
            if idx < len(pos[d]) and pos[d][idx] - start <= K:
                res.append(d)
                K -= pos[d][idx] - start
                start = pos[d][idx] + 1
                break
            
    return res


def main():
    T = int(input())
    for _ in range(T):
        A = list(map(int, list(input().decode().strip())))
        K = int(input())
        res = solve(A, K)
        print(*res, sep='')


if __name__ == '__main__':
    main()

