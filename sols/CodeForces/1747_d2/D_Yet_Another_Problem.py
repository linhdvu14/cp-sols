''' D. Yet Another Problem
https://codeforces.com/contest/1747/problem/D
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

from bisect import bisect_left

# parity of 1s in odd length array doesn't change after op
def main():
    N, Q = list(map(int, input().split()))
    A = list(map(int, input().split()))

    pos = [IntKeyDict(), IntKeyDict()]
    xor, zero = [0], [0]
    x = z = 0
    for i, a in enumerate(A): 
        x ^= a
        if a == 0: z += 1
        xor.append(x)
        zero.append(z)
        if x not in pos[i & 1]: pos[i & 1][x] = []
        pos[i & 1][x].append(i)
    
    def calc(l, r):
        z = zero[r + 1] - zero[l]
        if z == r - l + 1: return 0
        if xor[r + 1] ^ xor[l] != 0: return -1
        if (r - l + 1) & 1: return 1

        # even seg
        if r - l == 1: return -1
        if A[l] == 0 or A[r] == 0: return 1

        # need odd zero prefix
        x = xor[l]
        if x not in pos[l & 1]: return -1
        j = bisect_left(pos[l & 1][x], l)
        if j < len(pos[l & 1][x]) and pos[l & 1][x][j] <= r: return 2
        return -1
    
    res = []
    for _ in range(Q):
        l, r = list(map(int, input().split()))
        res.append(calc(l - 1, r - 1))
    
    print(*res, sep='\n')


if __name__ == '__main__':
    main()

