''' C. Quiz Master
https://codeforces.com/contest/1777/problem/C
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

MAX = 10**5
FACS = [[] for _ in range(MAX + 1)]

for a in range(1, MAX + 1):
    small, big = [], []
    s = 1
    while s * s < a:
        b, r = divmod(a, s)
        if not r:
            small.append(s)
            big.append(b)
        s += 1
    if s * s == a: small.append(s)
    FACS[a] = small + big[::-1]


def solve(N, M, A):
    A.sort()
    
    res = INF 
    cnt = IntKeyDict()
    l = 0
    for r, a in enumerate(A):
        for f in FACS[a]:
            if f > M: break 
            cnt[f] = cnt.get(f, 0) + 1
        
        while l <= r and len(cnt) == M:
            res = min(res, A[r] - A[l])
            for f in FACS[A[l]]: 
                if f > M: break
                cnt[f] -= 1
                if not cnt[f]: cnt.pop(f)
            l += 1

    return res if res < INF else -1


def main():
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))
        A = list(map(int, input().split()))
        res = solve(N, M, A)
        print(res)


if __name__ == '__main__':
    main()

