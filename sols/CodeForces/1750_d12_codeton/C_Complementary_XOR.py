''' C. Complementary XOR
https://codeforces.com/contest/1750/problem/C
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

def solve(N, A, B):
    res = []

    if all(a + b == 1 for a, b in zip(A, B)): 
        res.append((1, N))
        A = B[:]
    
    if not A == B: return False, []

    cnt = 0
    for i, a in enumerate(A):
        if a == 1: 
            res.append((i + 1, i + 1))
            cnt += 1
    
    if cnt % 2: res.extend([(1, N), (1, 1), (2, N)])

    return True, res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().decode().strip()))
        B = list(map(int, input().decode().strip()))
        r1, r2 = solve(N, A, B)
        if r1: 
            print('YES')
            print(len(r2))
            for t in r2: print(*t)
        else:
            print('NO')


if __name__ == '__main__':
    main()

