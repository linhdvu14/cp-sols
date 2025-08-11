''' D. Meta-set
https://codeforces.com/contest/1735/problem/D
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

# knowing 2 eles in set determines last ele
# each meta-set has exactly 2 sets; the sets are distinct except for a common pivot
# count num sets containing each pivot and pick 2

def solve(N, K, cards):
    known = set(tuple(c) for c in cards)

    res = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if j == i: continue
            ck = []
            for (vi, vj) in zip(cards[i], cards[j]):
                if vi == vj: ck.append(vi)
                else: ck.append(3 - vi - vj)
            if tuple(ck) in known: cnt += 1
        cnt //= 2
        res += cnt * (cnt - 1) // 2

    return res


def main():
    N, K = list(map(int, input().split()))
    cards = [list(map(int, input().split())) for _ in range(N)]
    res = solve(N, K, cards)
    print(res)


if __name__ == '__main__':
    main()

