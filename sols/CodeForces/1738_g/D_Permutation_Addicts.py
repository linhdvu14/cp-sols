''' D. Permutation Addicts
https://codeforces.com/contest/1738/problem/D
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

def solve(N, B):
    if all(b == 0 for b in B): return 0, list(range(1, N + 1))
    if all(b == N + 1 for b in B): return N, list(range(1, N + 1))

    adj = [[] for _ in range(N + 1)]
    head1, head2 = [], []
    for x, y in enumerate(B):
        x += 1
        if y == 0: head1.append(x)
        elif y == N + 1: head2.append(x)
        else: adj[y].append(x)
    
    assert not (head1 and head2)

    # glue edges together
    A = []
    cur = head1 + head2
    while True:
        tail = None
        for u in cur:
            if len(adj[u]) == 0: A.append(u)
            else: tail = u
        if not tail: break
        A.append(tail)
        cur = adj[tail]

    # calc K
    leq = 0
    for x in A:
        y = B[x - 1]
        if x < y: leq += 1

    return leq, A


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        B = list(map(int, input().split()))
        k, res = solve(N, B)
        print(k)
        print(*res)


if __name__ == '__main__':
    main()

