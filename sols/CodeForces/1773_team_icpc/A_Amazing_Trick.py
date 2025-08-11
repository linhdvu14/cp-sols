''' A. Amazing Trick
https://codeforces.com/contest/1773/problem/A
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

from itertools import permutations

def solve(N, A):
    pos = [-1] * N
    for i, a in enumerate(A): pos[a - 1] = i
    
    P, Q = [-1] * N, [-1] * N
    rem = set(list(range(N)))
    save = min(N, 4)
    for i in range(N - save):
        bad = []
        while True:
            a = rem.pop()
            if a == i or a == pos[i]: 
                bad.append(a)
            else:
                P[a], Q[i] = pos[i] + 1, a + 1
                break 
        for a in bad: rem.add(a)

    for p in permutations(rem):
        for i, a in zip(list(range(N - save, N)), p):
            if a == i or a == pos[i]:
                break
        else:
            for i, a in zip(list(range(N - save, N)), p):
                P[a] = pos[i] + 1
                Q[i] = a + 1
            return 'Possible', P, Q
    
    return 'Impossible', [], []



def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        r1, r2, r3 = solve(N, A)
        print(r1)
        if r2: print(*r2)
        if r3: print(*r3)


if __name__ == '__main__':
    main()
