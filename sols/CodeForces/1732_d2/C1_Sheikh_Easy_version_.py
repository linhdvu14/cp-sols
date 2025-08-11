''' C1. Sheikh (Easy version)
https://codeforces.com/contest/1732/problem/C1
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

# binary search
def solve_1(N, Q, A, queries):
    assert queries == [[1, N]]

    pref_sum, pref_xor = [0], [0]
    for a in A:
        pref_sum.append(pref_sum[-1] + a)
        pref_xor.append(pref_xor[-1] ^ a)
    
    def f(l, r): return pref_sum[r + 1] - pref_sum[l] - (pref_xor[r + 1] ^ pref_xor[l])
    
    res_l, res_r, res_v = 0, N - 1, f(0, N - 1)
    for l in range(N):
        v = f(l, N - 1)
        if v < res_v: continue

        r, lo, hi = N - 1, l, N - 1
        while lo <= hi:
            mi = (lo + hi) // 2
            if f(l, mi) == v:
                r = mi 
                hi = mi - 1
            else:
                lo = mi + 1
        
        if v > res_v: res_l, res_r, res_v = l, r, v
        if r - l < res_r - res_l: res_l, res_r = l, r

    return [[res_l + 1, res_r + 1]]

# 2 pointers
def solve_2(N, Q, A, queries):
    assert queries == [[1, N]]

    s = x = 0
    for a in A: 
        s += a 
        x ^= a 
    tar = s - x

    # l1 < l2 < r2 < r1; f(l2, r2) <= f(l1, r2) < f(l1, r1)
    res_l, res_r = 0, N - 1
    r = -1
    for l in range(N):
        if r < l: r, s, x = l, A[l], A[l]
        while r < N - 1 and s - x < tar:
            r += 1
            s += A[r]
            x ^= A[r]
        if s - x < tar: break 
        if r - l < res_r - res_l: res_l, res_r = l, r
        s -= A[l]
        x ^= A[l]
    
    return [[res_l + 1, res_r + 1]]


solve = solve_2

def main():
    T = int(input())
    for _ in range(T):
        N, Q = list(map(int, input().split()))
        A = list(map(int, input().split()))
        queries = [list(map(int, input().split())) for _ in range(Q)]
        res = solve(N, Q, A, queries)
        for t in res: print(*t)


if __name__ == '__main__':
    main()

