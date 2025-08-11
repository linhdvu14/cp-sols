''' D. Prefixes and Suffixes
https://codeforces.com/contest/1730/problem/D
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

# consider A and B' = reverse(B)
# - can swap A[i] with B'[i]
# - can rotate any subsegment A[i:j] and B'[i:j] by the same shift -> can make any order

def solve(N, A, B):
    par = {}
    for a, b in zip(A, B[::-1]):
        if a > b: a, b = b, a 
        par[a, b] = par.get((a, b), 0) ^ 1
    
    odd = sum(1 for v in par.values() if v == 1)
    if odd == 0: return True
    if odd > 1 or N % 2 == 0: return False 
    
    for (a, b), v in par.items():
        if v == 1 and a == b:
            return True 
    
    return False



def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = input().decode().strip()
        B = input().decode().strip()
        res = solve(N, A, B)
        print('YES' if res else 'NO')


if __name__ == '__main__':
    main()
