''' F. Kirei and the Linear Function
https://codeforces.com/contest/1729/problem/F
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

def solve(S, W, Q, queries):
    N = len(S)
    S = list(map(int, S))
    
    pref = [0]
    for a in S: pref.append(pref[-1] + a)
    
    idx = [[] for _ in range(9)]
    for i in range(N - W + 1):
        s = (pref[i + W] - pref[i]) % 9
        idx[s].append(i + 1)
    
    res = [(-1, -1) for _ in range(Q)]
    for qi, (l, r, k) in enumerate(queries):
        v = pref[r] - pref[l - 1]
        cand = (INF, INF)
        for r1 in range(9):
            if not idx[r1]: continue
            r2 = (k - r1 * v) % 9
            if r2 != r1 and idx[r2]: cand = min(cand, (idx[r1][0], idx[r2][0]))
            elif r2 == r1 and len(idx[r1]) > 1: cand = min(cand, (idx[r1][0], idx[r1][1]))
        if cand != (INF, INF): res[qi] = cand

    return res


def main():
    T = int(input())
    for _ in range(T):
        S = input().decode().strip()
        W, Q = list(map(int, input().split()))
        queries = [list(map(int, input().split())) for _ in range(Q)]
        res = solve(S, W, Q, queries)
        for r in res: print(*r)


if __name__ == '__main__':
    main()

