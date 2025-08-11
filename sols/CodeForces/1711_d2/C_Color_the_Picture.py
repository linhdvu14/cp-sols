''' C. Color the Picture
https://codeforces.com/contest/1711/problem/C
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') not in [None, '0']

if DEBUG:
    from inspect import currentframe, getframeinfo
    from re import search

def debug(*args):
    if not DEBUG: return
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
    def get(self, k, default=None): return super().get(k^self.rand, default)
    def keys(self): return [k^self.rand for k in super().keys()]
    def items(self): return [(k^self.rand, v) for k, v in super().items()]


INF = float('inf')

# -----------------------------------------

def solve(R, C, K, A):    
    def is_ok(R, C, K, A):
        cnt = [a // C for a in A]
        can = sum(c for c in cnt if c >= 2)
        if can < R: return False
        if R % 2 and max(cnt) < 3: return False
        return True
        
    if is_ok(R, C, K, A): return 'Yes'
    if is_ok(C, R, K, A): return 'Yes'
    return 'No'


def main():
    T = int(input())
    for _ in range(T):
        R, C, K = list(map(int, input().split()))
        A = list(map(int, input().split()))
        out = solve(R, C, K, A)
        print(out)


if __name__ == '__main__':
    main()

