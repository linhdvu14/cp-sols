''' E. Fibonacci Strings
https://codeforces.com/contest/1719/problem/E
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

from heapq import heappush, heappop

MAX = 10**11
F = [1, 1]
FSUM = [1, 2]
while FSUM[-1] < MAX:
    F.append(F[-1] + F[-2])
    FSUM.append(FSUM[-1] + F[-1])


# https://en.m.wikipedia.org/wiki/Zeckendorf%27s_theorem
def solve(N, A):
    s = sum(A)
    idx = -1
    for i, fs in enumerate(FSUM):
        if fs == s: 
            idx = i 
            break
    if idx == -1: return False

    # use max cnt letter different from last selected letter
    rem = []
    for i, a in enumerate(A): heappush(rem, (-a, i))

    prev = -1
    for f in F[:idx+1][::-1]:
        a, i = heappop(rem)
        a = -a 
        if i != prev and a >= f:
            if a > f: heappush(rem, (f - a, i))
            prev = i
            continue
            
        if not rem: return False

        b, j = heappop(rem)
        b = -b 
        if j != prev and b >= f:
            if b > f: heappush(rem, (f - b, j))
            prev = j 
            heappush(rem, (-a, i))
            continue

        return False

    return True


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        res = solve(N, A)
        print('YES' if res else 'NO')


if __name__ == '__main__':
    main()

