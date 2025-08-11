''' D. Color with Occurrences
https://codeforces.com/contest/1714/problem/D
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

INF = float('inf')

# -----------------------------------------

def solve_mle(S, N, strs):
    L = len(S)
    mp = {s: i+1 for i, s in enumerate(strs)}

    # 1e6
    right = [-1] * L
    for l in range(L):
        for r in range(l+1, L+1):
            if S[l:r] in mp:
                right[l] = r

    res = []
    r = 0
    while r < L:
        nr, nl = max((right[l], l) for l in range(r+1)) # 1e4
        if nr == -1: return []
        res.append((mp[S[nl:nr]], nl+1))  # 1e4
        r = nr
    
    return res


# 1e6 / test
def solve(S, N, strs):
    res = []
    r = 0
    while r < len(S):
        mx = (-1, -1, -1)
        for l in range(r+1):
            for i, s in enumerate(strs):
                if r < l+len(s) <= len(S) and S[l:l+len(s)] == s:
                    mx = max(mx, (l+len(s), i+1, l+1))
                    debug(r, l, s, mx)
        if mx[0] == -1: return []
        res.append((mx[1], mx[2]))
        r = mx[0]
    return res



def main():
    T = int(input())
    for _ in range(T):
        S = input().decode().strip()
        N = int(input())
        strs = [input().decode().strip() for _ in range(N)]
        out = solve(S, N, strs)
        if not out:
            print(-1)
        else:
            print(len(out))
            for tup in out: print(*tup)


if __name__ == '__main__':
    main()

 