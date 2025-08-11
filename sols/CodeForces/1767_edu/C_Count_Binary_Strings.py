''' C. Count Binary Strings
https://codeforces.com/contest/1767/problem/C
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

MOD = 998244353

def solve(N, grid):
    # dp[i][j] = num ways to place chars 1..i (1-index) s.t. j < i is last index s.t. S[j] != S[i]
    # and conditions for all strings ending at k <= i are satisfied
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[1][0] = 2 if grid[0][0] != 2 else 0

    for i in range(2, N + 1):
        for j in range(i):
            # place S[i - 1] at S[i], checking all conditions ending at i satisfied
            dp[i][j] = (dp[i][j] + dp[i - 1][j]) % MOD
            if any((grid[k][i - 1] == 1 and k <= j - 1) or (grid[k][i - 1] == 2 and k > j - 1) for k in range(i)): dp[i][j] = 0

            # place S[i - 1] ^ 1 at S[i]
            dp[i][i - 1] = (dp[i][i - 1] + dp[i - 1][j]) % MOD
            if any((grid[k][i - 1] == 1 and k <= i - 2) or (grid[k][i - 1] == 2 and k > i - 2) for k in range(i)): dp[i][i - 1] = 0

    res = sum(dp[-1]) % MOD
    return res


def main():
    N = int(input())
    grid = [[-1] * i + list(map(int, input().split())) for i in range(N)]
    res = solve(N, grid)
    print(res)


if __name__ == '__main__':
    main()

