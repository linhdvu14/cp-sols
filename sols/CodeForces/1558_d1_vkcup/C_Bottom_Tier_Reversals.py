''' C. Bottom-Tier Reversals
https://codeforces.com/contest/1558/problem/C
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

# reversal preserves parity of position
# put pair of (n, n-1), (n-2, n-3), ... in order
#    7 a b 6 c d e
#    b a 7 6 c d e
#    e d c 6 7 a b
#    7 6 c d e a b
#    b a e d c 6 7

def solve(N, A):
    res = []
    for a1 in range(N, 1, -2):
        # put a1 at 0
        for i, a in enumerate(A):
            if a == a1:
                if i & 1: return -1, []
                res.append(i + 1)
                A[:i+1] = A[:i+1][::-1]
                break 

        i0 = -1
        for i, a in enumerate(A):
            if a == a1 - 1: 
                if i & 1 == 0: return -1, []
                i0 = i
                break

        # 7 a b 6 c d e -> b a 7 6 c d e
        res.append(i0)
        A[:i0] = A[:i0][::-1]
        i1 = i0 - 1

        # b a 7 6 c d e -> e d c 6 7 a b
        res.append(a1)
        A[:a1] = A[:a1][::-1]
        i1 = a1 - 1 - i1

        # e d c 6 7 a b -> 7 6 c d e a b
        res.append(i1 + 1)
        A[:i1+1] = A[:i1+1][::-1]

        # 7 6 c d e a b -> b a e d c 6 7
        res.append(a1)
        A[:a1] = A[:a1][::-1]
        
    assert A == list(range(1, N + 1))
    assert all(a & 1 for a in res)
    assert len(res) <= 5 * N // 2
    return len(res), res



def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        r1, r2 = solve(N, A)
        print(r1)
        if r2: print(*r2)


if __name__ == '__main__':
    main()

