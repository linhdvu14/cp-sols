''' E. Decomposition
https://codeforces.com/contest/1766/problem/E
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

from collections import defaultdict

# each 0 adds 1 for each subarray containing it
# excluding 0s, decomposition has at most 3 subseq with these ending values
STATES = [
    (None, None, None),
    (1, None, None), (2, None, None), (3, None, None),
    (1, 2, None), (2, 1, None), (3, 1, None), (3, 2, None),
    (1, 1, None), (2, 2, None),
    (2, 2, 1), (1, 1, 2),
]

def solve(N, A):
    # num subarrays ending here with state s
    dp = defaultdict(int); dp[None, None, None] = 1

    res = zero = 0
    for i, a in enumerate(A):
        if a == 0:
            res += (i + 1) * (N - i)
            zero += 1
        else:
            dp[None, None, None] += zero
            ndp = defaultdict(int); ndp[None, None, None] = 1
            for s in STATES:
                if not dp[s]: continue
                for j, b in enumerate(s):
                    if b and not (a & b): continue
                    if not b: res += dp[s] * (N - i)
                    ndp[s[:j] + (a, ) + s[j + 1:]] += dp[s]
                    break
            zero = 0
            dp = ndp
    
    return res


def truth(N, A):
    res = 0
    for i in range(N):
        splits = []
        for j in range(i, N):
            ok = 0
            for k, s in enumerate(splits):
                if s[-1] & A[j]:
                    splits[k].append(A[j])
                    ok = 1
                    break 
            if not ok: splits.append([A[j]])
            res += len(splits)
    
    return res



def main():
    N = int(input())
    A = list(map(int, input().split()))
    res = solve(N, A)
    print(res)


if __name__ == '__main__':
    main()

