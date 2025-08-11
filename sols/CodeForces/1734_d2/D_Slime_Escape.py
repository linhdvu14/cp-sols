''' D. Slime Escape
https://codeforces.com/contest/1734/problem/D
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

def solve(N, K, A):
    K -= 1
    if A[K] < 0: return False
    if K == 0 or K == N - 1: return True

    # r_jump[i] = min r s.t. sum(i..r) >= 0
    # r_req[i] = min bal required at i s.t. running bal from i..r_jump[i] >= 0
    # r_gain[i] = bal diff from i..r_jump[i]
    r_jump, r_req, r_gain = [N] * N, [0] * N, [0] * N
    i = K
    while i < N - 1:
        j = i + 1
        s = mns = A[j]
        while j < N - 1 and s < 0:
            j += 1
            s += A[j]
            mns = min(mns, s)
        r_jump[i] = j
        r_req[i] = -mns 
        r_gain[i] = s
        i = j

    l_jump, l_req, l_gain = [-1] * N, [0] * N, [0] * N
    i = K
    while i > 0:
        j = i - 1
        s = mns = A[j]
        while j > 0 and s < 0:
            j -= 1
            s += A[j]
            mns = min(mns, s)
        l_jump[i] = j
        l_req[i] = -mns 
        l_gain[i] = s
        i = j

    # jump in either direction while possible
    l = r = K
    bal = A[K]
    while True:
        if bal >= l_req[l]:
            bal += l_gain[l]
            l = l_jump[l]
            if l == -1: return True
        elif bal >= r_req[r]:
            bal += r_gain[r]
            r = r_jump[r]
            if r == N: return True
        else:
            return False


def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        A = list(map(int, input().split()))
        res = solve(N, K, A)
        print('YES' if res else 'NO')


if __name__ == '__main__':
    main()

