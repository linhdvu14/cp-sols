''' D. The Strongest Build
https://codeforces.com/contest/1574/problem/D
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

# best state (if not last) is one step away from some banned state

def main():
    N = int(input())
    items, cnt = [], []
    for _ in range(N):
        A = list(map(int, input().split()))
        cnt.append(A[0])
        items.append(A[1:])
    
    M = int(input())
    banned = set(tuple(map(int, input().split())) for _ in range(M))

    mx = (-INF, [])
    idx = tuple(c for c in cnt)
    if idx not in banned: mx = (sum(it[-1] for it in items), idx)

    for idx in banned:
        idx = list(idx)
        s = sum(items[i][idx[i] - 1] for i in range(N))
        for i in range(N):
            if idx[i] == 1: continue
            idx[i] -= 1
            t = tuple(idx)
            if t not in banned: 
                ns = s - items[i][idx[i]] + items[i][idx[i] - 1]
                mx = max(mx, (ns, t))
            idx[i] += 1
    
    return mx[1]


if __name__ == '__main__':
    out = main()
    print(*out)

