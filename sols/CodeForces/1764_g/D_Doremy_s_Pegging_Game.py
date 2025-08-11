''' D. Doremy's Pegging Game
https://codeforces.com/contest/1764/problem/D
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

# when stop
# - remaining points in range 0..x covering < semi-circle
# - last removed point in range 0..x reflected over center
# - previously removed points (inside/outside 0..x) can be permuted
def main():
    N, MOD = list(map(int, input().split()))

    fact, inv_fact = [1] * (N + 1), [1] * (N + 1)
    for i in range(1, N + 1): fact[i] = i * fact[i - 1] % MOD
    inv_fact[-1] = pow(fact[-1], MOD - 2, MOD)
    for i in range(N - 1, 0, -1): inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

    def nCk(n, k): return 0 if k > n else fact[n] * inv_fact[k] * inv_fact[n - k] % MOD

    res = 0
    for x in range(N // 2 + N % 2):
        last_rm = x + (1 - N % 2)
        prev_rm = N - x - 2
        ways = fact[prev_rm]
        for k in range(1, x): ways = (ways + nCk(x - 1, k) * fact[prev_rm + k]) % MOD
        res = (res + ways * last_rm) % MOD

    print(res * N % MOD)


if __name__ == '__main__':
    main()

