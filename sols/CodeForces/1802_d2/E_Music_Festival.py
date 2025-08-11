''' E. Music Festival
https://codeforces.com/contest/1802/problem/E
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

class FenwickTreeMax:
    '''basic 0-base max Fenwick tree for point update, range query'''
    def __init__(self, N):
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


def solve(N, As):
    vals = {0}
    ends = {}
    for i, A in enumerate(As):
        B = []
        for a in A:
            if not B or B[-1] < a: 
                B.append(a)
        As[i] = B 
        vals.update(B)
        if B[-1] not in ends: ends[B[-1]] = []
        ends[B[-1]].append(i)
    
    vals = sorted(list(vals))
    mp = {v: i for i, v in enumerate(vals)}
    
    # fw.query(i) = ans if all values <= mp[i]
    # each album can contribute a suffix
    fw = FenwickTreeMax(len(vals))

    best = 0
    for e in sorted(ends.keys()):
        for ia in ends[e]:
            A = As[ia]
            N = len(A)
            for i, a in enumerate(A):
                best = max(best, fw.query(mp[a] - 1) + N - i)
        fw.update(mp[e], best)

    return best


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        As = []
        for _ in range(N): 
            _ = int(input())
            As.append(list(map(int, input().split())))
        res = solve(N, As)
        print(res)


if __name__ == '__main__':
    main()

