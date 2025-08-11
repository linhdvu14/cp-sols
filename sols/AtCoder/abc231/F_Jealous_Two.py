''' F - Jealous Two
https://atcoder.jp/contests/abc231/tasks/abc231_f
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

INF = float('inf')

# -----------------------------------------


class FenwickTree:
    '''basic 0-base sum Fenwick tree for point update, range query'''
    def __init__(self, data):
        '''transform list into BIT'''
        self.val = data[:]
        for i in range(len(self.val)):
            j = i | (i + 1)
            if j < len(self.val):
                self.val[j] += self.val[i]

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

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    S = sorted(set(A + B))
    mp = {c: i for i, c in enumerate(S)}
    fw = FenwickTree([0] * len(mp))

    pos = {}
    for i, a in enumerate(A):
        if a not in pos: pos[a] = []
        pos[a].append(i)

    res = 0
    keys = sorted(pos.keys())
    for a in keys:  # assign a to A
        for i in pos[a]: fw.add(mp[B[i]], 1)
        for i in pos[a]: res += fw.query_range(mp[B[i]], len(mp)-1)
    
    print(res)



if __name__ == '__main__':
    main()

