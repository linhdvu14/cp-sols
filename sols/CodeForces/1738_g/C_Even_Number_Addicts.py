''' C. Even Number Addicts
https://codeforces.com/contest/1738/problem/C
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
    even = odd = 0
    for a in A: 
        if a % 2 == 0: even += 1
        else: odd += 1
    
    # dp[p][o][e] = whether can make parity p with o odds and e evens
    dp = [[[0] * (even + 1) for _ in range(odd + 1)] for _ in range(2)]
    for e in range(even + 1): dp[0][0][e] = 1
    for o in range(odd + 1): dp[((o + 1) // 2) % 2][o][0] = 1

    for o in range(1, odd + 1):
        for e in range(1, even + 1):
            p = o % 2
            for pb in [0, 1]:
                if not dp[pb][o - 1][e]: dp[(p - pb - 1) % 2][o][e] |= 1
                if not dp[pb][o][e - 1]: dp[(p - pb - 1) % 2][o][e] |= 1

    return dp[0][-1][-1]


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        res = solve(N, A)
        print('Alice' if res else 'Bob')


if __name__ == '__main__':
    main()

