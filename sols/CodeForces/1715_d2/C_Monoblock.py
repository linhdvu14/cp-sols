''' C. Monoblock
https://codeforces.com/contest/1715/problem/C 
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

def solve(N, Q, A, queries):
    if N == 1: return [1] * Q
    
    # each boundary adds 1 to each subarray containing it
    s = N * (N + 1) // 2
    for i in range(1, N):
        if A[i] != A[i-1]: 
            s += i * (N - i)

    res = []
    for i, x in queries:
        i -= 1
        if i > 0:
            if A[i] != A[i-1]: s -= i * (N - i)
            if x != A[i-1]: s += i * (N - i)
        if i < N - 1:
            if A[i + 1] != A[i]: s -= (i + 1) * (N - i - 1)
            if A[i + 1] != x: s += (i + 1) * (N - i - 1)
        A[i] = x
        res.append(s)
    
    return res



def main():
    N, Q = list(map(int, input().split()))
    A = list(map(int, input().split()))
    queries = [list(map(int, input().split())) for _ in range(Q)]
    out = solve(N, Q, A, queries)
    print(*out, sep='\n')
    

if __name__ == '__main__':
    main()

