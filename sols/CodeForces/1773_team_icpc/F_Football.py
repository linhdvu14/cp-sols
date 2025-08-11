''' F. Football
https://codeforces.com/contest/1773/problem/F
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

def main():
    N, a, b = int(input()), int(input()), int(input())
    if N == 1:
        print(0 if a != b else 1)
        print(f'{a}:{b}')
    elif a + b <= N:
        print(N - a - b)
        for _ in range(a): print('1:0')
        for _ in range(b): print('0:1')
        for _ in range(N - a - b): print('0:0')
    elif a == 0:
        print(0)
        for _ in range(N - 1): print('0:1')
        print(f'0:{b - N + 1}')
    elif b == 0:
        print(0)
        for _ in range(N - 1): print('1:0')
        print(f'{a - N + 1}:0')
    else:
        print(0)
        ca = max(min(a - 1, N - 2), 0)
        cb = max(min(b - 1, N - 2 - ca), 0)
        for _ in range(ca): print('1:0')
        for _ in range(cb): print('0:1')
        print(f'{a - ca}:0')
        print(f'0:{b - cb}')


if __name__ == '__main__':
    main()

