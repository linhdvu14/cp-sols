''' C2. Sheikh (Hard Version)
https://codeforces.com/contest/1732/problem/C2
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

# partition query seg Q into [Y, N] where Y is answer seg and N = Q - Y
# f(S) == f(S + [v]) iff xor(S) and v have no common set bits
# then xor(Y) and xor(N) have no common set bits
# then each pair in N have no common set bits (otherwise can add 1 or both to Y)
# -> N have at most 30 nonzero eles

from bisect import bisect_left, bisect_right

def solve(N, Q, A, queries):
    pref_sum, pref_xor = [0], [0]
    nonzeros = []
    for i, a in enumerate(A):
        pref_sum.append(pref_sum[-1] + a)
        pref_xor.append(pref_xor[-1] ^ a)
        if a: nonzeros.append(i)

    def f(l, r): return pref_sum[r + 1] - pref_sum[l] - (pref_xor[r + 1] ^ pref_xor[l])

    res = [None] * Q
    for qi, (l, r) in enumerate(queries):
        res[qi] = (l, l)

        l -= 1; r -= 1
        li0 = bisect_left(nonzeros, l)
        ri0 = bisect_right(nonzeros, r) - 1
        if li0 >= ri0: continue

        res_l, res_r, res_f = l, r, f(l, r)
        for li in range(li0, li0 + 31):
            if li > ri0 or f(nonzeros[li], r) < res_f: break
            for ri in range(ri0, ri0 - 32, -1):
                if li > ri: break
                score = f(nonzeros[li], nonzeros[ri])
                if score < res_f: break 
                if score > res_f or (score == res_f and nonzeros[ri] - nonzeros[li] < res_r - res_l):
                    res_l, res_r, res_f = nonzeros[li], nonzeros[ri], score

        res[qi] = (res_l + 1, res_r + 1)

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, Q = list(map(int, input().split()))
        A = list(map(int, input().split()))
        queries = [list(map(int, input().split())) for _ in range(Q)]
        res = solve(N, Q, A, queries)
        for t in res: print(*t)


if __name__ == '__main__':
    main()

