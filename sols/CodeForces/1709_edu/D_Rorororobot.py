''' D. Rorororobot
https://codeforces.com/contest/1709/problem/D
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

class SparseTableMin:
    def __init__(self, data, func=max):
        self.func = func
        self.data = [list(data)]
        i, n = 1, len(data)
        while 2 * i <= n:
            prev = self.data[-1]
            self.data.append([func(prev[j], prev[j + i]) for j in range(n - 2 * i + 1)])
            i <<= 1

    def query(self, l, r):
        '''func of data[l..r]; O(1)'''
        depth = (r - l + 1).bit_length() - 1
        return self.func(self.data[depth][l], self.data[depth][r - (1 << depth) + 1])


def solve(R, C, A, Q, queries):
    st = SparseTableMin(A, func=max)

    res = ['NO'] * Q
    for i, (r1, c1, r2, c2, k) in enumerate(queries):
        if (c1 - c2) % k or (r1 - r2) % k: continue
        if c1 == c2: res[i] = 'Yes'; continue
        
        top = r1 + (R - r1) // k * k
        if c1 > c2: c1, c2 = c2, c1
        if top > st.query(c1-1, c2-1): res[i] = 'YES'

    return res


def main():
    R, C = list(map(int, input().split()))
    A = list(map(int, input().split()))
    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]
    out = solve(R, C, A, Q, queries)
    print(*out, sep='\n')


if __name__ == '__main__':
    main()

