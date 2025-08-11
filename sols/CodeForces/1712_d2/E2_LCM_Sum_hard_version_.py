''' E2. LCM Sum (hard version)
https://codeforces.com/contest/1712/problem/E2
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

def get_lpf(N):
    lpf = [1] * (N + 1)
    primes = []
    for i in range(2, N+1):
        if lpf[i] == 1:
            lpf[i] = i
            primes.append(i)
        for p in primes:
            if p * i > N or lpf[i] < p: break
            lpf[p * i] = p 
    return lpf

MAX = 2 * 10**5
LPF = get_lpf(MAX)

def get_divisors(x):
    cur = [1]
    while x > 1:
        p, cnt = LPF[x], 0
        while x % p == 0:
            cnt += 1
            x //= p 
        nxt = []
        for d in cur:
            for i in range(1, cnt+1):
                nxt.append(d * p**i)
        cur.extend(nxt)
    return cur


class FenwickTree:
    '''basic 0-base sum Fenwick tree for point update, range query'''
    def __init__(self, data):
        '''transform list into BIT'''
        self.val = data[:]
        for i in range(len(self.val)):
            j = i | (i + 1)
            if j < len(self.val):
                self.val[j] += self.val[i]

    def __len__(self):
        return len(self.val)

    def query(self, i):
        '''prefix sum data[0..i]'''
        s = 0
        end = i + 1
        while end:
            s += self.val[end - 1]
            end &= end - 1  # 110 -> 100
        return s
    
    def query_range(self, l, r):
        '''range sum data[l..r]'''
        return self.query(r) - self.query(l-1)

    def add(self, i, x):
        '''point update data[i] += x'''
        while i < len(self.val):
            self.val[i] += x
            i |= i + 1   # 101 -> 110


def solve(segs, Q):
    res = [0] * Q
    fw = FenwickTree([0] * (MAX + 1)) # a -> num bad triplets in current range
    idx = sorted(list(range(Q)), key=lambda i: (segs[i][1], segs[i][0]))
    last = 1
    for i in idx:
        l, r = segs[i]
        for c in range(last, r+1):
            divs = sorted(get_divisors(c))[:-1]
            for j, a in enumerate(divs): fw.add(a, len(divs) - 1 - j)
            if c % 6 == 0: fw.add(c // 2, 1)
            if c % 15 == 0: fw.add(2 * c // 5, 1)
        res[i] = (r - l + 1) * (r - l) * (r - l - 1) // 6 - fw.query_range(l, r)
        last = r + 1

    return res


def main():
    Q = int(input())
    segs = [list(map(int, input().split())) for _ in range(Q)]
    out = solve(segs, Q)
    print(*out, sep='\n')


if __name__ == '__main__':
    main()

