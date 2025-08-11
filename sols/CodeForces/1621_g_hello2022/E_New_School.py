''' E. New School
https://codeforces.com/contest/1621/problem/E
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') is not None

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


INF = float('inf')

# -----------------------------------------
class LazySegmentTree:
    def __init__(self, data, default=0, func=max):
        '''initialize the lazy segment tree with data'''
        self._default = default
        self._func = func

        self._len = len(data)                                   # orig data size
        self._size = _size = 1 << (self._len - 1).bit_length()  # tree size
        self._lazy = [0] * (2 * _size)                          # pending updates

        self.data = [default] * (2 * _size)                     # segment values
        self.data[_size:_size + self._len] = data               # store orig array in leaves
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[2*i], self.data[2*i + 1])

    def _push(self, idx):
        '''push pending update on idx to its children'''
        # clear parent update (data alr updated)
        q, self._lazy[idx] = self._lazy[idx], 0

        # push update to children and update children's data
        self._lazy[2 * idx] += q
        self._lazy[2 * idx + 1] += q
        self.data[2 * idx] += q
        self.data[2 * idx + 1] += q

    def _update(self, idx):
        '''update idx by pulling update from ancestors'''
        for i in reversed(range(1, idx.bit_length())):
            self._push(idx >> i)

    def _build(self, idx):
        '''make the changes to idx be known to its ancestors. CHANGE HERE'''
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1]) + self._lazy[idx]
            idx >>= 1

    def add(self, start, stop, value):
        '''lazily add value to [start, stop)'''
        start = start_copy = start + self._size  # idx of segment [start, start] in self.data
        stop = stop_copy = stop + self._size
        while start < stop:
            if start & 1:
                self._lazy[start] += value
                self.data[start] += value
                start += 1
            if stop & 1:
                stop -= 1
                self._lazy[stop] += value
                self.data[stop] += value
            start >>= 1
            stop >>= 1

        # Tell all nodes above of the updated area of the updates
        self._build(start_copy)
        self._build(stop_copy - 1)

    def query(self, start, stop, default=0):
        '''func of data[start, stop)'''
        start += self._size
        stop += self._size

        # Apply all the lazily stored queries
        self._update(start)
        self._update(stop - 1)

        res = default
        while start < stop:
            if start & 1:
                res = self._func(res, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res = self._func(res, self.data[stop])
            start >>= 1
            stop >>= 1
        return res


MAX = 10**5 + 1
segtree = LazySegmentTree([0]*MAX, default=INF, func=min)

def solve(N, M, A, B):
    # calc group avg; round up as we want b <= a
    B_sum = [sum(b) for b in B]
    B_avg = [(sum(b) + len(b) - 1) // len(b) for b in B]

    # let tree store s[v] = (num teachers with age >= v) - (num students with age >= v)
    # want min(s[v]) >= 0 over all v
    for a in A: segtree.add(0, a+1, 1)  # increment s[0], s[1], ... s[a]
    for b in B_avg: segtree.add(0, b+1, -1)

    res = [[0]*len(b) for b in B]
    for g, b in enumerate(B):
        segtree.add(0, B_avg[g]+1, 1)
        for s, v in enumerate(b):
            new_avg = (B_sum[g] - v + len(b) - 2) // (len(b) - 1)
            segtree.add(0, new_avg+1, -1)
            if segtree.query(0, MAX, INF) >= 0: res[g][s] = 1
            segtree.add(0, new_avg+1, 1)
        segtree.add(0, B_avg[g]+1, -1)
    
    # reset segtree
    for a in A: segtree.add(0, a+1, -1)
    for b in B_avg: segtree.add(0, b+1, 1)

    return ''.join(''.join(map(str, g)) for g in res)


def main():
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))
        A = list(map(int, input().split()))
        B = []
        for _ in range(M):
            _ = input()
            b = list(map(int, input().split()))
            B.append(b)
        out = solve(N, M, A, B)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

