''' C. Interesting Sequence
https://codeforces.com/contest/1775/problem/C
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

BITS = 60

def solve(N, X):
    if not N & X == X: return -1

    msb_n = msb_diff = -1
    for i in range(BITS - 1, -1, -1):
        if (N >> i) & 1:
            if msb_n == -1: msb_n = i
            if (X >> i) & 1 == 0:
                msb_diff = i 
                break

    if msb_diff == -1: return N 

    msb_set = -1
    for i in range(msb_diff, msb_n):
        if (N >> i) & 1 == 0:
            msb_set = i 
            break 
    
    if msb_set == -1: return -1 if X != 0 else (1 << (msb_n + 1))

    res = 1 << msb_set
    for i in range(msb_n, msb_set, -1):
        if (N >> i) & 1:
            res |= 1 << i 

    for i in range(msb_set):
        if (X >> i) & 1:
            return -1

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, X = list(map(int, input().split()))
        res = solve(N, X)
        print(res)



if __name__ == '__main__':
    main()

