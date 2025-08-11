''' D. Reset K Edges
https://codeforces.com/contest/1739/problem/D
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

def solve(N, K, par):
    for i in range(1, N): par[i] -= 1

    # note par[i] < i
    def is_ok(k):
        need = 0
        depth = [0] * N
        for u in range(N - 1, 0, -1):
            if depth[u] == k - 1 and par[u] != 0:
                need += 1
            else:
                depth[par[u]] = max(depth[par[u]], depth[u] + 1)
        return need <= K

    res, lo, hi = -1, 1, N
    while lo <= hi:
        mi = (lo + hi) // 2
        if is_ok(mi):
            res = mi 
            hi = mi - 1
        else:
            lo = mi + 1

    return res




def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        par = [1] + list(map(int, input().split()))
        res = solve(N, K, par)
        print(res)


if __name__ == '__main__':
    main()

