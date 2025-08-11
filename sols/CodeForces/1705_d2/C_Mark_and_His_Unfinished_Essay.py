''' C. Mark and His Unfinished Essay
https://codeforces.com/contest/1705/problem/C
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
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

from bisect import bisect_right

def solve(N, C, Q, S, ops, queries):
    lefts = [1+N]  # ops[i] is responsible for idx lefts[i].. in final str
    for l, r in ops: lefts.append(lefts[-1] + r - l + 1)

    res = []
    for k in queries:
        while k > N:
            i = bisect_right(lefts, k) - 1
            k = ops[i][0] + k - lefts[i]
        res.append(S[k-1])

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, C, Q = list(map(int, input().split()))
        S = input().decode().strip()
        ops = [list(map(int, input().split())) for _ in range(C)]
        queries = [int(input()) for _ in range(Q)]
        out = solve(N, C, Q, S, ops, queries)
        print(*out, sep='\n')


if __name__ == '__main__':
    main()

