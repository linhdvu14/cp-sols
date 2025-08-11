''' B. Also Try Minecraft
https://codeforces.com/contest/1709/problem/B
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

def solve(N, M, A, queries):
    pref = [0]
    for i in range(N-1):
        d = max(0, A[i] - A[i+1])
        pref.append(pref[-1] + d)
    
    suff = [0]
    for i in range(N-1, 0, -1):
        d = max(0, A[i] - A[i-1])
        suff.append(suff[-1] + d)
    suff.reverse()

    res = []
    for i, j in queries:
        if i <= j: res.append(pref[j-1] - pref[i-1])
        else: res.append(suff[j-1] - suff[i-1])

    return res


def main():
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    queries = [list(map(int, input().split())) for _ in range(M)]
    out = solve(N, M, A, queries)
    print(*out, sep='\n')


if __name__ == '__main__':
    main()

