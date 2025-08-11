''' D. Ela and the Wiring Wizard
https://codeforces.com/contest/1737/problem/D
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

# https://codeforces.com/blog/entry/107567?#comment-960835
# after rewiring, optimal path has 1 edge connecting (1, n); otherwise can fold shortest edge
# iterate over this last edge

def solve(N, M, edges):
    edges = [(u - 1, v - 1, w) for u, v, w in edges]

    d1 = [[INF] * N for _ in range(N)] 
    for u in range(N): d1[u][u] = 0
    for u, v, _ in edges: d1[u][v] = d1[v][u] = 1
    
    for t in range(N):
        for u in range(N):
            for v in range(N):
                d1[u][v] = min(d1[u][v], d1[u][t] + d1[t][v])
    
    d2 = [INF] * N 
    for u in range(N):
        for x in range(N):
            d2[u] = min(d2[u], d1[u][x] + d1[x][0] + d1[x][N - 1])

    # case 1: u -> 1, v -> N, cand = (dist[u][1] + dist[v][N] + 1) * w
    # case 2: u -> x, v -> x, x -> 1, x -> N, cand = (dist[u][x] + dist[x][1] + dist[x][N] + 2) * w
    res = INF
    for u, v, w in edges:
        m = min(
            d1[u][0] + d1[v][N - 1] + 1,
            d1[v][0] + d1[u][N - 1] + 1,
            d2[u] + 2,
            d2[v] + 2,
        )
        res = min(res, m * w)

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))
        edges = [list(map(int, input().split())) for _ in range(M)]
        res = solve(N, M, edges)
        print(res)


if __name__ == '__main__':
    main()

