''' C. Set Construction
https://codeforces.com/contest/1761/problem/C
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

def solve_1(N, B):
    adj = [[] for _ in range(N)]
    deg = [0] * N

    for i in range(N):
        for j in range(N):
            if B[i][j] == '1':
                adj[i].append(j)
                deg[j] += 1
    
    res = [set([u + 1]) for u in range(N)]
    st = [u for u in range(N) if deg[u] == 0]
    while st:
        u = st.pop()
        for v in adj[u]:
            deg[v] -= 1
            if deg[v] >= 0: res[v] |= res[u]
            if deg[v] == 0: st.append(v)

    return res


def solve_2(N, B):
    res = [[i + 1] for i in range(N)]
    for i in range(N):
        for j in range(N):
            if B[i][j] == '1':
                res[j].append(i + 1)
    
    return res


solve = solve_2

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        B = [input().decode().strip() for _ in range(N)]
        res = solve(N, B)
        for row in res: print(len(row), *list(row))


if __name__ == '__main__':
    main()

