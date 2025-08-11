''' F. Build a Tree and That Is It
https://codeforces.com/contest/1714/problem/F
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
    def get(self, k, default=None): return super().get(k^self.rand, default)
    def keys(self): return [k^self.rand for k in super().keys()]
    def items(self): return [(k^self.rand, v) for k, v in super().items()]
    def __contains__(self, k): return super().__contains__(k^self.rand)

INF = float('inf')

# -----------------------------------------

# let 1 = root, w = lca(2, 3), d(w..1) = a, d(w..2) = b, d(w..3) = c
# a + b = d12, b + c = d23, c + a = d31
def solve(N, d12, d23, d31):
    s, r = divmod(d12 + d23 + d31, 2)
    if r: return []

    a, b, c = s - d23, s - d31, s - d12
    if a < 0 or b < 0 or c < 0 or a + b + c + 1 > N: return []

    def build(a, b, c, db, dc, N):
        res = []
    
        p, n = a, 4
        for _ in range(db - 1):
            res.append((p, n))
            p, n = n, n + 1
        res.append((p, b))
        
        p = a
        for _ in range(dc - 1):
            res.append((p, n))
            p, n = n, n + 1
        res.append((p, c))

        for i in range(n, N+1): res.append((a, i))
        assert len(res) == N-1
        return res

    if a == 0: return build(1, 2, 3, b, c, N)
    if b == 0: return build(2, 3, 1, c, a, N)
    if c == 0: return build(3, 1, 2, a, b, N)

    res = []
    
    p, n = 1, 4
    for _ in range(a):
        res.append((p, n))
        p, n = n, n+1
    
    w = p
    for _ in range(b-1):
        res.append((p, n))
        p, n = n, n+1
    res.append((p, 2))

    p = w
    for _ in range(c-1):
        res.append((p, n))
        p, n = n, n+1
    res.append((p, 3))

    for i in range(n, N+1): res.append((1, i))
    assert len(res) == N-1

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, d12, d23, d31 = list(map(int, input().split()))
        out = solve(N, d12, d23, d31)
        if not out: 
            print('NO')
        else:
            print('YES')
            for tup in out: print(*tup)


if __name__ == '__main__':
    main()

