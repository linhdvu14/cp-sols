''' D. 1-2-K Game
https://codeforces.com/contest/1194/problem/D
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


INF = float('inf')

# -----------------------------------------

def solve(N, K):
    if N == K: return 'Alice'
    if K % 3 and K != N: return 'Alice' if N % 3 else 'Bob'

    # K <= N, K % 3 == 0
    # losing positions are (K+1)m + 3n, except for (K+1)m + K
    N %= K + 1
    if N == K: return 'Alice'
    return 'Alice' if N % 3 else 'Bob'


def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        out = solve(N, K)
        print(out)


if __name__ == '__main__':
    main()

