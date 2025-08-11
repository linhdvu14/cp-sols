''' F. Range Update Point Query
https://codeforces.com/contest/1791/problem/F
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
        '''transform list into BIT'''
        self.val = [0] * N
    
    def add(self, i, x):
        '''point update data[i] += x'''
        while i < len(self.val):
            self.val[i] += x
            i |= i + 1   # 101 -> 111
    
    def query(self, i):
        '''prefix sum data[0..i]'''
        s = 0
        i += 1
        while i:
            s += self.val[i - 1]
            i &= i - 1  # 110 -> 100
        return s


def solve(N, Q, A, queries):
    ans = [[a] for a in A]
    for i, a in enumerate(A):
        while a >= 10:
            a = sum(int(c) for c in str(a))
            ans[i].append(a)
    
    fw = FenwickTree(N + 1)
    res = [] 
    for ts in queries:
        if len(ts) == 3:
            l, r = ts[1:]
            fw.add(l, 1)
            fw.add(r + 1, -1)
        else:
            i = ts[1] - 1
            c = fw.query(i + 1)
            if c < len(ans[i]): c = -1
            res.append(ans[i][c])

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, Q = list(map(int, input().split()))
        A = list(map(int, input().split()))
        queries = [list(map(int, input().split())) for _ in range(Q)]
        res = solve(N, Q, A, queries)
        print(*res, sep='\n')


if __name__ == '__main__':
    main()

