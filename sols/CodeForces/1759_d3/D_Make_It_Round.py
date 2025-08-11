''' D. Make It Round
https://codeforces.com/contest/1759/problem/D
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

def solve(n, m):
    two = five = 0
    tmp = n
    while tmp and tmp % 2 == 0:
        two += 1
        tmp //= 2
    while tmp and tmp % 5 == 0:
        five += 1
        tmp //= 5
    
    zero = min(two, five)
    two -= zero
    five -= zero 
    
    k = 1
    while five and k * 2 <= m:
        k *= 2 
        five -= 1
    while two and k * 5 <= m:
        k *= 5 
        two -= 1
    while k * 10 <= m: k *= 10
    res = n * k * (m // k)

    return res


def main():
    T = int(input())
    for _ in range(T):
        n, m = list(map(int, input().split()))
        res = solve(n, m)
        print(res)


if __name__ == '__main__':
    main()

