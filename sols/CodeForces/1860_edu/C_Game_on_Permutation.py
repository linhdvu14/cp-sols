''' C. Game on Permutation
https://codeforces.com/contest/1860/problem/C
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
        self.val = [-INF] * N

    def query(self, i):
        s = -INF
        end = i + 1
        while end:
            s = max(s, self.val[end - 1])
            end &= end - 1
        return s

    def update(self, i, x):
        while i < len(self.val):
            self.val[i] = max(self.val[i], x)
            i |= i + 1


def solve(N, P):
    res = 0
    fw = FenwickTree(N + 1)
    
    for a in P:
        win = fw.query(a - 1) == 0
        res += win 
        fw.update(a, win)

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        P = list(map(int, input().split()))
        res = solve(N, P)
        print(res)


if __name__ == '__main__':
    main()

