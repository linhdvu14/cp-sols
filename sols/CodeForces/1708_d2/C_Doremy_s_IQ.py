''' C. Doremy's IQ
https://codeforces.com/contest/1708/problem/C
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

# bal must change Q -> Q-1 -> Q-2 -> ... -> 0
# simulate from end of process
# best to increase earliest necessary

def solve(N, Q, A):
    res = [0] * N
    cur = 0
    for i in range(N-1, -1, -1):
        if A[i] <= cur: 
            res[i] = 1
        elif cur < Q:
            cur += 1
            if cur <= Q: res[i] = 1

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, Q = list(map(int, input().split()))
        A = list(map(int, input().split()))
        out = solve(N, Q, A)
        print(*out, sep='')


if __name__ == '__main__':
    main()


