''' G. Cut Substrings
https://codeforces.com/contest/1729/problem/G
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

MOD = 10**9 + 7

def solve(S, P):
    points = [i for i in range(len(S) - len(P) + 1) if S[i:i + len(P)] == P]
    if not points: return 0, 1

    # dp[i] = min ops and num ways to cover first i points using first i points
    dp = [(INF, 0) for _ in range(len(points) + 1)]
    dp[0] = (0, 1)
    
    for i in range(len(points)):
        for j in range(i, -1, -1):
            if points[i] - points[j] >= len(P): break
            k = j
            while k > 0 and points[j] - points[k-1] < len(P): k -= 1
            if dp[i+1][0] > 1 + dp[k][0]: dp[i+1] = (1 + dp[k][0], 0)
            if dp[i+1][0] == 1 + dp[k][0]: dp[i+1] = (1 + dp[k][0], (dp[i+1][1] + dp[k][1]) % MOD)

    return dp[-1]


def main():
    T = int(input())
    for _ in range(T):
        S = input().decode().strip()
        P = input().decode().strip()
        res = solve(S, P)
        print(*res)


if __name__ == '__main__':
    main()

