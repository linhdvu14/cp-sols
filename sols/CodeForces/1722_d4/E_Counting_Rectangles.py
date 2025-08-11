''' E. Counting Rectangles
https://codeforces.com/contest/1722/problem/E
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

MAX = 1005

def solve(N, Q, pts, queries):
    A = [[0] * MAX for _ in range(MAX)]
    for r, c in pts: A[r][c] += r * c

    # dp[r][c] = num pts inside (0, 0) and (r, c)
    dp = [[0] * MAX for _ in range(MAX)]
    for r in range(1, MAX):
        for c in range(1, MAX):
            dp[r][c] = dp[r-1][c] + dp[r][c-1] - dp[r-1][c-1] + A[r][c]
    
    res = []
    for r1, c1, r2, c2 in queries:
        s = dp[r2 - 1][c2 - 1] - dp[r2 - 1][c1] - dp[r1][c2 - 1] + dp[r1][c1]
        res.append(s)

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, Q = list(map(int, input().split()))
        pts = [list(map(int, input().split())) for _ in range(N)]
        queries = [list(map(int, input().split())) for _ in range(Q)]
        res = solve(N, Q, pts, queries)
        print(*res, sep='\n')


if __name__ == '__main__':
    main()

