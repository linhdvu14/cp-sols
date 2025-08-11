''' D. Mark and Lightbulbs
https://codeforces.com/contest/1705/problem/D
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

# a valid operation is equivalent to swapping adjacent (0, 1) or (-1, 0) on difference array

def solve(N, A, B):
    if A[0] != B[0]: return -1

    A = [A[i] - A[i-1] for i in range(1, N)]
    B = [B[i] - B[i-1] for i in range(1, N)]
    
    pa = [i for i, a in enumerate(A) if a != 0]
    pb = [i for i, b in enumerate(B) if b != 0]

    if len(pa) != len(pb): return -1
    if any(A[i] != B[j] for i, j in zip(pa, pb)): return -1

    return sum(abs(i - j) for i, j in zip(pa, pb))


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, list(input().decode().strip())))
        B = list(map(int, list(input().decode().strip())))
        out = solve(N, A, B)
        print(out)


if __name__ == '__main__':
    main()

