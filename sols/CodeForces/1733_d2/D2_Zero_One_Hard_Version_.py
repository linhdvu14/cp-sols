''' D2. Zero-One (Hard Version)
https://codeforces.com/contest/1733/problem/D2
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

def solve(N, X, Y, A, B):
    bad = [i for i, (a, b) in enumerate(zip(A, B)) if a != b]
    if not bad: return 0
    if len(bad) % 2: return -1

    if X >= Y:
        if len(bad) == 2 and bad[0] + 1 == bad[1]: return min(X, 2 * Y)
        return Y * len(bad) // 2

    # use all Y initially then try to save by converting to X
    # dp[i][0] = max save for 0..i, if use Y on (i, *)
    # dp[i][1] = max save for 0..i, if use X on (i..i-1)
    dp = [[0, 0] for _ in range(len(bad))]
    for i in range(1, len(bad)):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1])
        dp[i][1] = Y - (bad[i] - bad[i-1]) * X + dp[i-1][0]

    return Y * len(bad) // 2 - max(dp[-1])


def main():
    T = int(input())
    for _ in range(T):
        N, X, Y = list(map(int, input().split()))
        A = input().decode().strip()
        B = input().decode().strip()
        res = solve(N, X, Y, A, B)
        print(res)


if __name__ == '__main__':
    main()

