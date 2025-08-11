''' G. Gaining Rating
https://codeforces.com/contest/1772/problem/G
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

from bisect import bisect_right

# x kills A[i] iff x >= A[j] - j for all j <= i
def solve(N, X, Y, A):
    A.sort()
    if X < A[0]: return -1
    if N == 1: return Y - X

    pref = [A[0]]
    for i in range(1, N): pref.append(max(pref[-1], A[i] - i))

    res = 0
    while True: 
        win = bisect_right(pref, X)
        if win == N or Y - X <= win: return res + Y - X 
        gain = 2 * win - N
        if gain <= 0: return -1

        # peak X after completing r rounds is X + gain * r + win
        rounds = (min(Y - X - win, pref[win] - X) + gain - 1) // gain
        res += N * rounds 
        X += gain * rounds


def main():
    T = int(input())
    for _ in range(T):
        N, X, Y = list(map(int, input().split()))
        A = list(map(int, input().split()))
        res = solve(N, X, Y, A)
        print(res)


if __name__ == '__main__':
    main()

