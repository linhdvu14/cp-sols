''' G. SlavicG's Favorite Problem
https://codeforces.com/contest/1760/problem/G
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

def solve(N, a, b, edges):
    a -= 1; b -= 1

    adj = [[] for _ in range(N)]
    for u, v, w in edges:
        adj[u - 1].append((v - 1, w))
        adj[v - 1].append((u - 1, w))

    # reachable from a w/o passing b
    seen = set()
    st = [(a, -1, 0)]
    while st:
        u, p, x = st.pop()
        if u == b:
            if x == 0: return 'YES'
            continue
        seen.add(x)
        for v, w in adj[u]:
            if v == p: continue
            st.append((v, u, x ^ w))
    
    # reachable from b
    st = [(b, -1, 0)]
    while st:
        u, p, x = st.pop()
        if u != b and x in seen: return 'YES'
        for v, w in adj[u]:
            if v == p: continue
            st.append((v, u, x ^ w))

    return 'NO'


def main():
    T = int(input())
    for _ in range(T):
        N, a, b = list(map(int, input().split()))
        edges = [list(map(int, input().split())) for _ in range(N - 1)]
        res = solve(N, a, b, edges)
        print(res)


if __name__ == '__main__':
    main()

