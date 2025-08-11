''' C. Equal Frequencies
https://codeforces.com/contest/1782/problem/C
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
from string import ascii_lowercase

def solve(N, A):
    pos = {}
    for i, c in enumerate(A):
        if c not in pos: pos[c] = []
        pos[c].append(i)
    pos = sorted(pos.items(), key=lambda t: len(t[1]))

    def f(n):
        sz = N // n
        B = list(A)

        free = []
        for i in range(max(0, len(pos) - n)):
            free.extend(pos[i][1])
        
        chars = set(ascii_lowercase)
        for i in range(n):
            if i < len(pos):
                c, v = pos[-1 - i]
                chars.remove(c)
                if len(v) >= sz: 
                    free.extend(v[:len(v) - sz])
                else: 
                    for _ in range(sz - len(v)):
                        B[free.pop()] = c
            else:
                c = chars.pop()
                for _ in range(sz):
                    B[free.pop()] = c 
        
        need = sum(1 for a, b in zip(A, B) if a != b)
        return need, ''.join(B)
    
    res = (INF, '')
    for uniq in range(1, 27):
        if N % uniq: continue
        cand = f(uniq)
        res = min(res, cand)
    
    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = input().decode().strip()
        res = solve(N, A)
        print(*res, sep='\n')


if __name__ == '__main__':
    main()

