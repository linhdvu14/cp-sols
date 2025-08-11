''' B. BinCoin
https://codeforces.com/contest/1773/problem/B
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

MOD = 10**9 + 7

def main():
    N, K = list(map(int, input().split()))
    perms = [list(map(int, input().split())) for _ in range(K)]

    pow = [1]
    for _ in range(N): pow.append(pow[-1] * 2 % MOD)

    res = [-1] * N 
    rem = [[[[0, N - 1] for _ in range(K)], -1]]  # [](l, r), par
    while rem:
        bounds, par = rem.pop()

        l, r = bounds[0]
        if l == r: 
            res[perms[0][l] - 1] = par 
            continue
        
        seen = IntKeyDict()  # val -> hash sets
        for k, (l, r) in enumerate(bounds):
            s = 0
            for i in range(l, r):
                s = (s + pow[perms[k][i]]) % MOD
                v = perms[k][i + 1]
                if v not in seen: seen[v] = set()
                seen[v].add(s)
        
        # root has at most 2 distinct hash sets
        root = -1
        for v, ss in seen.items():
            if len(ss) <= 2:
                root = v 
                break 
        
        res[root - 1] = par 

        # split and recurse
        nxt = [[], []]
        pivot = perms[0][bounds[0][0]]

        for k, (l, r) in enumerate(bounds):
            idx = 0
            for i in range(l, r + 1):
                v = perms[k][i]
                if v == pivot: idx = 1
                elif v == root: 
                    nxt[idx].append([l, i - 1])
                    nxt[1 - idx].append([i + 1, r])
        
        if nxt[0]: rem.append([nxt[0], root])
        if nxt[1]: rem.append([nxt[1], root])


    print(*res)
                



if __name__ == '__main__':
    main()

