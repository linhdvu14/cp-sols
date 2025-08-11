''' B. Array merging
https://codeforces.com/contest/1831/problem/B
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

def solve(N, A, B):
    def f(A):
        cnt = {}
        c = 0
        for i, a in enumerate(A):
            if i and a != A[i - 1]: c = 0
            c += 1
            cnt[a] = max(cnt.get(a, 0), c)
        return cnt
    
    ca, cb = f(A), f(B)
    res = 1
    for k in set(list(ca.keys()) + list(cb.keys())):
        res = max(res, ca.get(k, 0) + cb.get(k, 0))

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        res = solve(N, A, B)
        print(res)


if __name__ == '__main__':
    main()

