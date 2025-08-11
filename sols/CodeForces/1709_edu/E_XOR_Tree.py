''' E. XOR Tree
https://codeforces.com/contest/1709/problem/E 
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') not in [None, '0']

if DEBUG:
    from inspect import currentframe, getframeinfo
    from re import search

def debug(*args):
    if not DEBUG: return
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
    def get(self, k, default=None): return super().get(k^self.rand, default)
    def keys(self): return [k^self.rand for k in super().keys()]
    def items(self): return [(k^self.rand, v) for k, v in super().items()]


INF = float('inf')

# -----------------------------------------

def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    adj = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v = list(map(int, input().split()))
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)

    # u should be replaced if:
    # 1. some v in u's subtree has xor(v..u) == 0, i.e xor(0..v) ^ xor(0..u) == A[u]
    # 2. some v1, v2 in 2 different subtrees of u has xor(v1..u..v2) == 0, i.e. xor(0..v1) ^ xor(0..v2) == A[u]
    # if replace u, then all paths through u will be good, i.e. can cut off u's subtree
    @bootstrap
    def dfs(u, p=-1, x=0):
        x ^= A[u]       # xor(0..u)
        big = set([x])  # xor(0..v) for v in u's subtree
        ok = True
        for v in adj[u]:  # small to large merging
            if v == p: continue
            small = yield dfs(v, u, x)
            if len(small) > len(big): small, big = big, small 
            ok &= not any(x ^ A[u] in big for x in small)
            big |= small

        if not ok:
            nonlocal res
            res += 1
            big.clear()
        yield big

    res = 0
    dfs(0)

    print(res)


if __name__ == '__main__':
    main()

