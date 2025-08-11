''' D. Koxia and Game
https://codeforces.com/contest/1770/problem/D
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

MOD = 998244353

# consider each connected component
# - 0 loop (tree) -> N ways (propagate from leaf x N roots)
# - 1 loop -> N ways if self-loop, else 2 ways
# - 2+ loops -> 0 way
def solve_1(N, A, B):
    adj = [[] for _ in range(N)]
    for e, (u, v) in enumerate(zip(A, B)):
        adj[u - 1].append((v - 1, e))
        if u != v: adj[v - 1].append((u - 1, e))

    @bootstrap
    def dfs(u):
        nonlocal loops, self_loops, nodes
        seen[u] = 1
        nodes += 1
        for v, e in adj[u]:
            if seen_edge[e]: continue
            seen_edge[e] = 1
            if not seen[v]: 
                yield dfs(v)
            else:
                loops += 1
                if v == u: self_loops += 1
        yield None
    
    res = 1
    seen = [0] * N
    seen_edge = [0] * N
    for u in range(N):
        if seen[u]: continue
        loops = self_loops = nodes = 0
        dfs(u)
        if loops == 0: res = res * nodes % MOD
        elif loops == 1: res = res * N % MOD if self_loops else res * 2 % MOD 
        else: return 0
    
    return res


# each component has nodes == edges
def solve_2(N, A, B):
    adj = [[] for _ in range(N)]
    for u, v in zip(A, B):
        adj[u - 1].append(v - 1)
        adj[v - 1].append(u - 1)
    
    def is_ok(u):
        nodes = edges = 0
        st = [u]
        seen[u] = 1
        while st:
            u = st.pop()
            nodes += 1
            edges += len(adj[u])
            for v in adj[u]:
                if seen[v]: continue
                seen[v] = 1
                st.append(v)
        return nodes == edges // 2
    
    loop = sum(1 for u, v in zip(A, B) if u == v)
    comp = 0
    seen = [0] * N
    for u in range(N):
        if seen[u]: continue
        if not is_ok(u): return 0
        comp += 1    
    
    return pow(N, loop, MOD) * pow(2, comp - loop, MOD) % MOD



solve = solve_2

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        res = solve(N, A, B)
        print(res)


if __name__ == '__main__':
    main()

