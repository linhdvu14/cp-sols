''' F. MEX vs MED
https://codeforces.com/contest/1744/problem/F
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

# when mex = m, seg has {0, 1, ..., m-1}, no {m}, at most m eles in {m+1, m+2, ..., N-1}
def solve(N, A):
    pos = [-1] * N 
    for i, a in enumerate(A): pos[a] = i

    # num ways to select (x, y) s.t. 0 <= x <= a, 0 <= y <= b, x + y <= m
    # draw out in 2d
    def f(a, b, m):
        if m < 0: return 0
        m = min(m, a + b)
        
        # x=0, y=0..m   -> m+1
        # x=1, y=0..m-1 -> m
        # x=m, y=0      -> 1
        res = (m + 1) * (m + 2) // 2

        # x=a+1, y=0..m-a-1 -> m-a
        # x=m, y=0          -> 1
        if a < m: res -= (m - a) * (m - a + 1) // 2
        if b < m: res -= (m - b) * (m - b + 1) // 2

        return res

    res = m = 0
    l = r = pos[0]
    while m <= N - 1:
        l, r = min(l, pos[m]), max(r, pos[m])
        while m <= N - 1 and l <= pos[m] <= r: m += 1
        if m == N: break

        # extend outside [l, r]
        nl = l - pos[m] - 1 if pos[m] < l else l
        nr = pos[m] - r - 1 if pos[m] > r else N - 1 - r
        res += f(nl, nr, m - (r - l + 1 - m))

    return res + 1



def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        res = solve(N, A)
        print(res)


if __name__ == '__main__':
    main()
