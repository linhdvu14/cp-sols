''' G1. In Search of Truth (Easy Version)
https://codeforces.com/contest/1840/problem/G1
'''

import functools
import os, sys
input = sys.stdin.readline  # strip() if str; io.BytesIO(os.read(0,os.fstat(0).st_size)).readline doesn't work
output = functools.partial(print, flush=True)

DEBUG = os.environ.get('debug') not in [None, '0']

def debug(*args):   
    if not DEBUG: return
    from inspect import currentframe, getframeinfo
    from re import search
    frame = currentframe().f_back
    s = getframeinfo(frame).code_context[0]
    r = search(r"\((.*)\)", s).group(1)
    vnames = r.split(', ')
    var_and_vals = [f'{var}={val}' for var, val in zip(vnames, args)]
    prefix = f'{currentframe().f_back.f_lineno:02d}: '
    print(f'{prefix}{", ".join(var_and_vals)}')

INF = float('inf')

# -----------------------------------------
from random import randrange
class IntKeyDict(dict):
    rand = randrange(1 << 62)
    def __setitem__(self, k, v): super().__setitem__(k^self.rand, v)
    def __getitem__(self, k): return super().__getitem__(k^self.rand)
    def __contains__(self, k): return super().__contains__(k^self.rand)
    def __repr__(self): return str({k: v for k, v in self.items()})
    def get(self, k, default=None): return super().get(k^self.rand, default)
    def keys(self): return [k^self.rand for k in super().keys()]
    def items(self): return [(k^self.rand, v) for k, v in super().items()]
    def pop(self, k): return super().pop(k^self.rand)


MAX = 10**6
global PERM, PTR

def ask(k):
    global PTR
    output(f'+ {k}')
    if DEBUG: PTR = (PTR + k) % len(PERM); res = PERM[PTR]; output(res)
    else: res = int(input())
    return res


def guess(ans):
    output(f'! {ans}')
    if DEBUG:
        assert ans == len(PERM), f'fail {PERM=} {len(PERM)=} got {ans=}'
        output('OK\n')


def solve(x):
    pos = IntKeyDict()
    pos[x] = 0
    sq = int(MAX**0.5) + 1

    for i in range(sq):
        x = ask(1)
        if x in pos: guess(i + 1); return  
        else: pos[x] = i + 1
    
    for i in range(sq):
        x = ask(sq)
        if x in pos:
            res = sq * (i + 2) - pos[x]
            guess(res); return


def main():    
    x = int(input())
    solve(x)


def gen():
    import random
    random.seed(123)

    global PERM, PTR
    for _ in range(100):
        n = random.randint(1, MAX)
        PTR = 0
        PERM = list(range(1, n + 1))
        random.shuffle(PERM)
        if DEBUG: output(PERM[PTR])
        solve(PERM[PTR])
    output('tests passed')
 

if __name__ == '__main__':
    if DEBUG: gen()
    else: main()