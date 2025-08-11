''' C. Yet Another Tournament
https://codeforces.com/contest/1783/problem/C
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

# ranks w/o prep are: me < 0 < 1 < 2 < ... < N - 1
# can take player i's place if
# - can win any i + 1 players
# - can win i - 1 players and player i
def solve(N, M, A):
    if N == 1: return 1 if M >= A[0] else 2
    idx = sorted(list(range(N)), key=lambda i: A[i])

    # s1[i] = sum of i smallest vals
    s1 = [0]
    for i in idx: s1.append(s1[-1] + A[i])

    # s2[i] = sum of A[i] and i-1 smallest vals except i
    s2 = [INF, A[1]]
    used = [0] * N 
    cur = 0
    for i in range(2, N):
        pos = idx[i - 2]
        cur += A[pos]
        used[pos] = 1
        if used[i]: s2.append(cur + A[idx[i - 1]])
        else: s2.append(cur + A[i])

    res = -1
    for i in range(N):
        if M >= s1[i + 1] or M >= s2[i]:
            res = i

    return N - res


def main():
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))
        A = list(map(int, input().split()))
        res = solve(N, M, A)
        print(res)


if __name__ == '__main__':
    main()

