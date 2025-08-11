''' D. Maximum AND
https://codeforces.com/contest/1721/problem/D 
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

def solve_1(N, A, B):
    res = 0
    
    groups = [(A, B)]
    for i in range(29, -1, -1):
        ok = True
        ngroups = []
        for A, B in groups:
            A0, A1 = [], []
            B0, B1 = [], []
            for a in A: 
                if (a >> i) & 1: A1.append(a)
                else: A0.append(a)
            for b in B:
                if (b >> i) & 1: B1.append(b)
                else: B0.append(b)
            if len(A0) != len(B1): ok = False; break 
            if A0: ngroups.append((A0, B1))
            if A1: ngroups.append((A1, B0))
        if ok: 
            res |= 1 << i
            groups = ngroups

    return res


def solve_2(N, A, B):
    def is_ok(pref):
        ta = [a & pref for a in A]
        tb = [~b & pref for b in B]
        return sorted(ta) == sorted(tb)

    res = 0
    for i in range(29, -1, -1):
        cand = res | (1 << i)
        if is_ok(cand): res = cand 
    
    return res


solve = solve_2

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        res = solve(N, A, B)
        print(res)


if __name__ == '__main__':
    main()
