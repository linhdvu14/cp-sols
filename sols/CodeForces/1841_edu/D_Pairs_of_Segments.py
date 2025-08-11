''' D. Pairs of Segments
https://codeforces.com/contest/1841/problem/D
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
    def __init__(self, N):
        self.N = N
        self.val = [0] * N
 
    def query(self, i):
        '''prefix max data[0..i]'''
        s = -INF
        end = i + 1
        while end:
            s = max(s, self.val[end - 1])
            end &= end - 1
        return s
 
    def update(self, i, x):
        '''point update data[i] = x; require x >= desired value'''
        while i < len(self.val):
            self.val[i] = max(self.val[i], x)
            i |= i + 1
 
 
def solve_1(N, segs):
    segs.sort(key=lambda t: (t[1], t[0]))
    vals = [-1] + sorted(list(set(x for l, r in segs for x in [l, r])))
    MAX = len(vals)
    mp = {v: i for i, v in enumerate(vals)}
 
    # fq.query(x) = max pairs s.t. last point <= x
    fw = FenwickTree(MAX)
 
    res = N 
    for i2, (l2, r2) in enumerate(segs):
        for i1 in range(i2 - 1, -1, -1):
            l1, r1 = segs[i1]
            if r1 < l2: break 
            fw.update(mp[r2], fw.query(mp[min(l2, l1)] - 1) + 2)
 
    res = N - fw.query(MAX - 1)
    return res


# greedily pick largest r1, smallest r2
def solve_2(N, segs):
    segs.sort(key=lambda t: t[1])

    cnt = 0
    r1 = r2 = -1
    for l, r in segs:
        if l <= r2: continue
        if l <= r1:
            cnt += 1
            r2 = r 
        else:
            r1 = r

    return N - 2 * cnt


solve = solve_2

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        segs = [list(map(int, input().split())) for _ in range(N)]
        res = solve(N, segs)
        print(res)


if __name__ == '__main__':
    main()

