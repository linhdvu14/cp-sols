''' D. Boris and His Amazing Haircut
https://codeforces.com/contest/1779/problem/D 
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

class SparseTable:
    def __init__(self, data, func=max):
        self.func = func
        self.data = [list(data)]
        d, n = 1, len(data)
        while 2 * d <= n:
            cur = self.data[-1]
            nxt = [func(cur[i], cur[i + d]) for i in range(n - 2 * d + 1)]
            self.data.append(nxt)
            d <<= 1

    def query(self, l, r):
        '''func of data[l..r]; O(1)'''
        d = (r - l + 1).bit_length() - 1
        return self.func(self.data[d][l], self.data[d][r - (1 << d) + 1])


def solve(N, A, B, M, X):
    pos = IntKeyDict()
    for i, (a, b) in enumerate(zip(A, B)):
        if b > a: return 'NO'
        if b < a: 
            if b not in pos: pos[b] = []
            pos[b].append(i)
    
    st = SparseTable(B, func=max)

    # place longest x, to cover as many keys as possible
    X.sort()
    rem = sorted(pos.keys())
    while rem:
        b = rem[-1]
        while X and X[-1] > b: X.pop()
        if not X or X[-1] < b: return 'NO'
        x = X.pop()
        r = pos[b].pop()
        while pos[b] and st.query(pos[b][-1], r) <= x: pos[b].pop()
        if not pos[b]: rem.pop()

    return 'YES'


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        M = int(input())
        X = list(map(int, input().split()))
        res = solve(N, A, B, M, X)
        print(res)


if __name__ == '__main__':
    main()

