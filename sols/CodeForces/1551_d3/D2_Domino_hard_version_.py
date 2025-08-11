''' D2. Domino (hard version)
https://codeforces.com/contest/1551/problem/D2
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

def solve(R, C, hor):
    ver = R * C // 2 - hor
    if R % 2 == C % 2 == 0 and hor % 2 == 1: return 'NO', []
    if R % 2 == 1 and not (hor >= C // 2 and (hor - C // 2) % 2 == 0): return 'NO', []
    if C % 2 == 1 and not (ver >= R // 2 and (ver - R // 2) % 2 == 0): return 'NO', []

    res = [['.'] * C for _ in range(R)]
    if R % 2 == 1:
        for c in range(C//2):
            if c % 2 == 0: res[-1][2*c] = res[-1][2*c+1] = 'a'
            else: res[-1][2*c] = res[-1][2*c+1] = 'b'
            hor -= 1
    if C % 2 == 1:
        for r in range(R//2):
            if r % 2 == 0: res[2*r][-1] = res[2*r+1][-1] = 'c'
            else: res[2*r][-1] = res[2*r+1][-1] = 'd'
            ver -= 1

    HOR, VER = 'efgh', 'ijkl'
    i = j = 0
    for r in range(R//2):
        for c in range(C//2):
            if hor:
                while (r and res[2*r-1][2*c] == HOR[i]) or (c and res[2*r][2*c-1] == HOR[i]): i = (i + 1) % 4
                res[2*r][2*c] = res[2*r][2*c+1] = HOR[i]
                res[2*r+1][2*c] = res[2*r+1][2*c+1] = HOR[(i + 1) % 4]
                i = (i + 2) % 4
                hor -= 2
            else:
                while (r and res[2*r-1][2*c] == VER[j]) or (c and res[2*r][2*c-1] == VER[j]): j = (j + 1) % 4
                res[2*r][2*c] = res[2*r+1][2*c] = VER[j]
                res[2*r][2*c+1] = res[2*r+1][2*c+1] = VER[(j + 1) % 4]
                j = (j + 2) % 4
                ver -= 2
    
    return 'YES', res


def main():
    T = int(input())
    for _ in range(T):
        R, C, K = list(map(int, input().split()))
        r1, r2 = solve(R, C, K)
        print(r1)
        for r in r2: print(*r, sep='')


if __name__ == '__main__':
    main()

