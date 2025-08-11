''' D. Flexible String Revisit
https://codeforces.com/contest/1778/problem/D
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
    def pop(self, k): return super().pop(k^self.rand)

INF = float('inf')

# -----------------------------------------

MOD = 998244353
MAX = 10**6
INV = [1] * (MAX + 1)
for i in range(2, MAX + 1): INV[i] = MOD - MOD // i * INV[MOD % i] % MOD

def solve(N, A, B):
    bad = sum(1 for a, b in zip(A, B) if a != b)
    if not bad: return 0

    # f(x) = (f(x - 1) - 1 - (x - 1) / N * f(x - 2)) * N / (N - x + 1)
    # f(x) = m * f(0) + a
    coef = [[0, 0]] * (N + 1)
    coef[1] = [1, 0]
    for i in range(2, N + 1):
        m1, a1 = coef[i - 1]
        m2, a2 = coef[i - 2]
        z = N * INV[N - i + 1] % MOD
        coef[i] = [
            (m1 - (i - 1) * INV[N] % MOD * m2) * z % MOD,
            (a1 - 1 - (i - 1) * INV[N] % MOD * a2) * z % MOD,
        ]

    # f(N) = 1 + f(N - 1)
    m1, a1 = coef[N]
    m2, a2 = coef[N - 1]
    f0 = (a2 - a1 + 1) * INV[m1 - m2] % MOD if m1 > m2 else (a1 - 1 - a2) * INV[m2 - m1] % MOD
    
    m, a = coef[bad]
    return (m * f0 + a) % MOD


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = input().decode().strip()
        B = input().decode().strip()
        res = solve(N, A, B)
        print(res)


if __name__ == '__main__':
    main()

