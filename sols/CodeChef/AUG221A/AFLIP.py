''' Angled Flip
https://www.codechef.com/AUG221A/problems/AFLIP
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

# flipping along main diagonal -> can swap a cell with any cell on its main diagonal

def solve(R, C, A, B):
    if R == 1 or C == 1: return A == B

    cnt = [{}, {}]
    for r in range(R):
        for c in range(C):
            p = (r + c) & 1
            cnt[p][A[r][c]] = cnt[p].get(A[r][c], 0) + 1
            cnt[p][B[r][c]] = cnt[p].get(B[r][c], 0) - 1
    
    return all(c == 0 for c in cnt[0].values()) and all(c == 0 for c in cnt[1].values())


def main():
    T = int(input())
    for _ in range(T):
        R, C = list(map(int, input().split()))
        A = [list(map(int, input().split())) for _ in range(R)]
        B = [list(map(int, input().split())) for _ in range(R)]
        out = solve(R, C, A, B)
        print('YES' if out else 'NO')


if __name__ == '__main__':
    main()

