''' C. Moamen and XOR
https://codeforces.com/contest/1557/problem/C
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') not in [None, '0']

if DEBUG:
    from inspect import currentframe, getframeinfo
    from re import search

def debug(*args):
    if not DEBUG: return
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
    def get(self, k, default=None): return super().get(k^self.rand, default)
    def keys(self): return [k^self.rand for k in super().keys()]
    def items(self): return [(k^self.rand, v) for k, v in super().items()]


INF = float('inf')

# -----------------------------------------

MOD = 10**9 + 7
POW = [pow(2, i, MOD) for i in range(2*10**5 + 1)]

def solve_1(N, B):
    dp = [1] + [0] * B  # ans for b bits

    for b in range(1, B+1):
        # current bit is all 1s
        if N % 2 == 0: dp[b] = pow(POW[b-1], N, MOD)
        else: dp[b] = dp[b-1]

        # current bit has some 0s
        dp[b] += dp[b-1] * (POW[N-1] - (N % 2 == 0))
        dp[b] %= MOD
    
    return dp[B]

 
def solve_2(N, B):
    # dp[b][l] = num ways to pick b msb, whether alr have AND > XOR
    dp = [[0, 0] for _ in range(B + 1)]
    dp[0][0] = 1

    for b in range(1, B+1):
        dp[b][1] = dp[b-1][1] * POW[N]

        # current bit is all 1s
        if N % 2 == 0: dp[b][1] += dp[b-1][0]
        else: dp[b][0] = dp[b-1][0]

        # current bit has some 0s
        dp[b][0] += dp[b-1][0] * (POW[N-1] - (N % 2 == 0))
        
        dp[b][0] %= MOD
        dp[b][1] %= MOD
    
    return sum(dp[B]) % MOD


solve = solve_2

def main():
    T = int(input())
    for _ in range(T):
        N, B = list(map(int, input().split()))
        out = solve(N, B)
        print(out)


if __name__ == '__main__':
    main()

