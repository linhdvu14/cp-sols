''' F. Smaller
https://codeforces.com/contest/1742/problem/F
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

from heapq import heappush, heappop, heapify

def solve(Q, queries):
    cnt = [[1] + [0] * 25, [1] + [0] * 25]

    def f(cnt_a, cnt_b):
        ha = [(i, c) for i, c in enumerate(cnt_a) if c]
        hb = [(-i, c) for i, c in enumerate(cnt_b) if c]
        heapify(ha); heapify(hb)

        while ha and hb:
            a, ca = heappop(ha)
            b, cb = heappop(hb); b = -b 
            if a < b: return 'YES'
            if a > b: return 'NO'
            if ca > cb: heappush(ha, (a, ca - cb))
            if ca < cb: heappush(hb, (-b, cb - ca))
        if not hb: return 'NO'
        return 'YES'

    res = []
    for t, k, x in queries:
        t, k = int(t) - 1, int(k)
        for c in x: cnt[t][ord(c) - ord('a')] += k
        res.append(f(cnt[0], cnt[1]))

    return res


def main():
    T = int(input())
    for _ in range(T):
        Q = int(input())
        queries = [input().decode().strip().split() for _ in range(Q)]
        res = solve(Q, queries)
        print(*res, sep='\n')


if __name__ == '__main__':
    main()

