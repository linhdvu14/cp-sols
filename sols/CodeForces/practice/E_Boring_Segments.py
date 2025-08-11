''' E. Boring Segments
https://codeforces.com/contest/1555/problem/E
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

class LazySegmentTree:
    def __init__(self, init_arr, default=0, func=max):
        ''' initialize the lazy segment tree with data
        func must return one of its input (e.g. min/max, not mult/add/sub)
        '''
        self.default = default
        self.func = func

        n = len(init_arr)                              # orig data size
        self.offset = sz = 1 << (n - 1).bit_length()   # offset to orig data
        self.lazy = [0] * (2 * sz)                     # pending updates

        self.val = [default] * (2 * sz)                # segment values
        self.val[sz : sz + n] = init_arr
        for i in reversed(range(sz)):
            self.val[i] = func(self.val[2*i], self.val[2*i + 1])

    def _push(self, i):
        '''push pending update on idx to its children'''
        # clear parent update (data alr updated)
        q, self.lazy[i] = self.lazy[i], 0

        # push update to children and update children's data
        self.lazy[2*i] += q
        self.lazy[2*i + 1] += q
        self.val[2*i] += q
        self.val[2*i + 1] += q

    def _update(self, i):
        '''update idx i by pulling update from ancestors'''
        for b in reversed(range(1, i.bit_length())):
            self._push(i >> b)

    def _build(self, i):
        '''make the changes to idx i be known to its ancestors. CHANGE HERE'''
        i >>= 1
        while i:
            self.val[i] = self.func(self.val[2*i], self.val[2*i + 1]) + self.lazy[i]
            i >>= 1

    def query(self, l, r):
        '''range query l..r'''
        l += self.offset
        r += self.offset + 1

        # apply all the lazily stored queries
        self._update(l)
        self._update(r - 1)

        res = self.default
        while l < r:
            if l & 1:
                res = self.func(res, self.val[l])
                l += 1
            if r & 1:
                r -= 1
                res = self.func(res, self.val[r])
            l >>= 1
            r >>= 1
        return res

    def add(self, l, r, x):
        '''lazily add x to l..r'''
        l = l_orig = l + self.offset
        r = r_orig = r + self.offset + 1
        while l < r:
            if l & 1:
                self.lazy[l] += x
                self.val[l] += x
                l += 1
            if r & 1:
                r -= 1
                self.lazy[r] += x
                self.val[r] += x
            l >>= 1
            r >>= 1

        # tell all nodes above of the updated area of the updates
        self._build(l_orig)
        self._build(r_orig - 1)

    def set(self, l, r, x):  # added
        '''lazily set x to l..r'''
        l = l_orig = l + self.offset
        r = r_orig = r + self.offset + 1
        while l < r:
            if l & 1:
                self.lazy[l] = x
                self.val[l] = x
                l += 1
            if r & 1:
                r -= 1
                self.lazy[r] = x
                self.val[r] = x
            l >>= 1
            r >>= 1
 
        # tell all nodes above of the updated area of the updates
        self._build(l_orig)
        self._build(r_orig - 1)

    def __repr__(self):
        return 'LazySegmentTree({})'.format(self.data)


# 2 pointers
# sort segs by weight
# for each candidate mn, extend to smallest mx s.t. 1..M is covered

def solve(N, M, segs):    
    segtree = LazySegmentTree([0] * M, default=INF, func=min)  # model gap between i and i+1
    segtree.add(0, 0, 1)
    segs.sort(key=lambda tup: tup[2])

    res = INF
    end = -1
    for l, r, w in segs:
        while segtree.query(0, M-1) < 1 and end + 1 < N:
            end += 1
            segtree.add(segs[end][0], segs[end][1]-1, 1)
        if segtree.query(0, M-1) < 1: break
        res = min(res, segs[end][2] - w)
        segtree.add(l, r-1, -1)

    return res


def main():
    M, N = list(map(int, input().split()))
    segs = [list(map(int, input().split())) for _ in range(M)]
    res = solve(M, N, segs)
    print(res)


if __name__ == '__main__':
    main()

