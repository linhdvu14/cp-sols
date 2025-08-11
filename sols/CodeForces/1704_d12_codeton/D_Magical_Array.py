''' D. Magical Array
https://codeforces.com/contest/1704/problem/D
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

# op 1 doesn't change sum of prefix sums
# op 2 reduces sum of prefix sums by 1
def solve(N, M, A):
    idx = {}
    for i, a in enumerate(A):
        p = s = 0
        for ele in a:
            p += ele
            s += p
        if s not in idx: idx[s] = []
        if len(idx[s]) < 2: idx[s].append(i+1)
    
    reg = odd = -1
    for k, v in idx.items():
        if len(v) == 1: odd = k
        else: reg = k

    return idx[odd][0], reg - odd


def main():
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))
        A = [list(map(int, input().split())) for _ in range(N)]
        out = solve(N, M, A)
        print(*out)


if __name__ == '__main__':
    main()

