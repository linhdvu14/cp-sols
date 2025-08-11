''' K. King’s Puzzle
https://codeforces.com/contest/1773/problem/K
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

def solve(N, K):
    if K == N == 1: return 'YES', []
    if K == N: return 'NO', []
    if K == 1:
        res = [(i, i + 1) for i in range(1, N)]
        if N > 2: res.append((N, 1))
        return 'YES', res

    res = [(N, i) for i in range(1, N)]
    for i in range((K - 2) // 2):
        res.extend((N - 1 - i, j) for j in range(i + 2, N - 1 - i))
    
    if K % 2: res.append((N - 1 - (K - 2) // 2, N - 2 - (K - 2) // 2))

    return 'YES', res


def main():
    N, K = list(map(int, input().split()))
    r1, r2 = solve(N, K)
    print(r1)
    if r1 == 'YES': 
        print(len(r2))
        for t in r2: print(*t)

if __name__ == '__main__':
    main()
