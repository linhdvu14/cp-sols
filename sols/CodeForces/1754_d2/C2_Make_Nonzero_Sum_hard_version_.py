''' C2. Make Nonzero Sum (hard version)
https://codeforces.com/contest/1754/problem/C2
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

def solve(N, A):
    if sum(A) % 2: return -1, []
    if set(A) == {0}: return 1, [(1, N)]

    res = []

    nonzero = [i for i in range(N) if A[i]]
    for i in range(0, len(nonzero), 2):
        l, r = nonzero[i], nonzero[i + 1]
        if not res and l: res.append((0, l - 1))
        elif res and res[-1][-1] < l - 1: res.append((res[-1][-1] + 1, l - 1))

        if A[l] + A[r] * (1 if l % 2 == r % 2 else -1) == 0: res.append((l, r))
        elif A[l] == A[r]: res.extend([(l, r - 2), (r - 1, r)])
        else: res.extend([(l, r - 1), (r, r)])
    
    if res[-1][-1] < N - 1: res.append((res[-1][-1] + 1, N - 1))

    return len(res), [(l + 1, r + 1) for l, r in res]


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        r1, r2 = solve(N, A)
        print(r1)
        for t in r2: print(*t)


if __name__ == '__main__':
    main()

