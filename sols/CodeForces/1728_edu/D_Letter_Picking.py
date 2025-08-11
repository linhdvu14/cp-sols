''' D. Letter Picking
https://codeforces.com/contest/1728/problem/D
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

def solve(S):
    N = len(S)

    # dp[i][j] = 1 if S[i:j] win, 0 if draw
    dp = [[1] * (N+1) for _ in range(N+1)]
    for i in range(N+1): dp[i][i] = 0
    for i in range(N-1): dp[i][i+2] = 0 if S[i] == S[i+1] else 1
    
    for d in range(4, N+1, 2):
        for i in range(N-d+1):
            c1 = S[i] == S[i+d-1] and dp[i+1][i+d-1] == 0
            c2 = S[i] == S[i+1] and dp[i+2][i+d] == 0
            c3 = S[i+d-1] == S[i+d-2] and dp[i][i+d-2] == 0
            if (c1 or c2) and (c1 or c3): dp[i][i+d] = 0

    return 'Alice' if dp[0][N] == 1 else 'Draw'


def main():
    T = int(input())
    for _ in range(T):
        S = input().decode().strip()
        res = solve(S)
        print(res)


if __name__ == '__main__':
    main()

