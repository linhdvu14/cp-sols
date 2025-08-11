''' D. Fixed Prefix Permutations
https://codeforces.com/contest/1792/problem/D
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
    def pop(self, k): return super().pop(k^self.rand)

INF = float('inf')

# -----------------------------------------

class Trie:
    def __init__(self):
        self.root = IntKeyDict()
    
    def insert(self, perm):
        pos = [-1] * len(perm)
        for i, a in enumerate(perm): pos[a - 1] = i 
        n = self.root 
        for p in pos:
            if p not in n: n[p] = IntKeyDict()
            n = n[p]
    
    def query(self, perm):
        n = self.root
        for i, p in enumerate(perm):
            p -= 1
            if p not in n: return i 
            n = n[p]
        return i + 1


def solve(N, M, perms):
    trie = Trie()
    for p in perms: trie.insert(p)
    res = [trie.query(p) for p in perms]
    return res


def main():
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))
        perms = [list(map(int, input().split())) for _ in range(N)]
        res = solve(N, M, perms)
        print(*res)


if __name__ == '__main__':
    main()

