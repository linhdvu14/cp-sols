''' D. 2+ doors
https://codeforces.com/contest/1715/problem/D
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

BITS = 30

def solve_tle(N, Q, ops):
    ops = [(i-1, j-1, x) if i < j else (j-1, i-1, x) for i, j, x in ops]
    ops.sort()
 
    res = [0] * N
    bad = [0] * N
    for i, j, x in ops:
        bad[i] |= ~x 
        bad[j] |= ~x
        if i == j: res[i] = x
 
    need = [[] for _ in range(BITS)]
    for i, j, x in ops:
        for b in range(BITS):
            if (x >> b) & 1 and (res[i] >> b) & 1 == (res[j] >> b) & 1 == 0:
                if (bad[i] >> b) & 1: res[j] |= 1 << b 
                elif (bad[j] >> b) & 1: res[i] |= 1 << b 
                else: need[b].append((i, j))
 
    for b in range(BITS):
        for i, j in need[b]:
            if (res[i] >> b) & 1 == (res[j] >> b) & 1 == 0:
                res[j] |= 1 << b
 
    return res


def solve(N, Q, ops):
    m = [(1 << BITS) - 1] * N
    adj = [[] for _ in range(N)]
    for i, j, x in ops:
        i -= 1; j -= 1
        adj[i].append((j, x))
        adj[j].append((i, x))
        m[i] &= x 
        m[j] &= x
    
    for i in range(N):
        n = 0
        for j, x in adj[i]:
            if j == i: n = x 
            else: n |= x & (~m[j])
        m[i] = n
    
    return m


def main():
    N, Q = list(map(int, input().split()))
    ops = [list(map(int, input().split())) for _ in range(Q)]
    out = solve(N, Q, ops)
    print(*out)


if __name__ == '__main__':
    main()


