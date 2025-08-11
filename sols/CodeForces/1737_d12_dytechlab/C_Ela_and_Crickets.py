''' C. Ela and Crickets
https://codeforces.com/contest/1737/problem/C
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

def solve(N, p0, p1, p2, px):
    pts = [p0, p1, p2]  
    for i, (r, c) in enumerate(pts):
        cnt_r = cnt_c = 0
        for rr, cc in pts:
            if r == rr: cnt_r += 1
            if c == cc: cnt_c += 1
        if cnt_r == cnt_c == 2:
            pts = [pts[i]] + [pts[j] for j in range(3) if j != i]
            if pts[0][0] != pts[1][0]: pts[1], pts[2] = pts[2], pts[1]
            break
    p0, p1, p2 = pts
    
    def is_ok_diag(p1, p2, px):
        for r, c in [p1, p2, px]:
            if not (0 <= r < N and 0 <= c < N):
                return False
        if p1[0] + p1[1] == p2[0] + p2[1] == px[0] + px[1]: return True 
        if p1[0] - p1[1] == p2[0] - p2[1] == px[0] - px[1]: return True 
        return False
    
    if is_ok_diag(p1, p2, px): return 'YES'
    if px[0] == p0[0] or px[1] == p0[1]: return 'YES'
    if p0 in [(0, 0), (0, N - 1), (N - 1, 0), (N - 1, N - 1)]: return 'NO'
    
    if (px[0] + px[1]) % 2 != (p0[0] + p0[1]) % 2: return 'YES'
    if px[0] % 2 == p0[0] % 2 and px[1] % 2 == p0[1] % 2: return 'YES'
    return 'NO'


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        r1, c1, r2, c2, r3, c3 = list(map(int, input().split()))
        rx, cx = list(map(int, input().split()))
        res = solve(N, (r1 - 1, c1 - 1), (r2 - 1, c2 - 1), (r3 - 1, c3 - 1), (rx - 1, cx - 1))
        print(res)


if __name__ == '__main__':
    main()

