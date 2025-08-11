''' D. Chip Move
https://codeforces.com/contest/1716/problem/D
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
    def get(self, k, default=None): return super().get(k^self.rand, default)
    def keys(self): return [k^self.rand for k in super().keys()]
    def items(self): return [(k^self.rand, v) for k, v in super().items()]

INF = float('inf')

# -----------------------------------------

MOD = 998244353 

# dp[k][n] = num ways to reach n when last move length is k
# dp[k][n] = dp[k-1][n-k] + dp[k-1][n-2k] + dp[k-1][n-3k] + ...
#          = dp[k-1][n-k] + dp[k][n-k]

def solve(N, k):
    res = [0] * (N + 1)
    dp = [0] * (N + 1)
    dp[0] = 1

    m = 0  # min n reachable with the current num steps
    while m <= N:
        m += k
        ndp = [0] * (N + 1)
        for n in range(k, N+1):
            ndp[n] = (ndp[n] + dp[n - k] + ndp[n - k]) % MOD
            res[n] = (res[n] + ndp[n]) % MOD
        dp = ndp
        k += 1

    return res[1:]


def main():
    N, K = list(map(int, input().split()))
    out = solve(N, K)
    print(*out)


if __name__ == '__main__':
    main()

