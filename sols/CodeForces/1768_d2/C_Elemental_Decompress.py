''' C. Elemental Decompress
https://codeforces.com/contest/1768/problem/C
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

def solve(N, A):
    pos = [[] for _ in range(N + 1)]
    for i, a in enumerate(A): pos[a].append(i)

    B, C = [-1] * N, [-1] * N 
    fb, fc = [], []
    for a in range(N, 0, -1):
        if len(pos[a]) > 2: 
            return 'NO', [], []
        elif len(pos[a]) == 2: 
            i, j = pos[a]
            B[i] = C[j] = a 
            fc.append(i)
            fb.append(j)
        elif len(pos[a]) == 1:
            i = pos[a][0]
            if fc: 
                j = fc.pop()
                B[i] = C[j] = a 
                fc.append(i)
            else:
                B[i] = C[i] = a
        else:
            if not fb or not fc: return 'NO', [], []
            i, j = fb.pop(), fc.pop()
            B[i] = C[j] = a 
            
    return 'YES', B, C


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        a, b, c = solve(N, A)
        print(a)
        if b: print(*b)
        if c: print(*c)



if __name__ == '__main__':
    main()

