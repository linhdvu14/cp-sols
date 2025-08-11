''' Problem A2: Consecutive Cuts - Chapter 2
https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-1/problems/A2
'''

import os, sys
input = sys.stdin.readline
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

def kmp(T, P):
    M, N = len(P), len(T)

    lps = [0] * M 
    j = 0
    for i in range(1, M):
        while j and P[i] != P[j]: j = lps[j-1]
        if P[i] == P[j]: j += 1
        lps[i] = j

    res = []
    j = 0
    for i in range(N):
        while j and T[i] != P[j]: j = lps[j-1]
        if T[i] == P[j]: j += 1
        if j == M:
            res.append(i - M + 1)
            j = lps[j-1]

    return res


def solve(N, K, A, B):
    matches = kmp(A*2, B)
    if not matches: return False

    if K == 0: return A == B
    if N == 2: return (A == B and K % 2 == 0) or (A != B and K % 2 == 1) or len(set(A)) == 1
    if K == 1: return A != B or len(matches) > 2

    return True


def main():
    T = int(input())
    for t in range(T):
        N, K = list(map(int, input().split()))
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        res = solve(N, K, A, B)
        print(f'Case #{t+1}:', 'YES' if res else 'NO')


if __name__ == '__main__':
    main()

