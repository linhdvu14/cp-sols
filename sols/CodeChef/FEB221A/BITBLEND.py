''' Bitwise Blend
https://www.codechef.com/FEB221A/problems/BITBLEND
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
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


INF = float('inf')

# -----------------------------------------

# A have alternating parity
def solve(N, A):
    # 0 first
    i1 = -1
    for i in range(1, N, 2):
        if A[i] % 2 == 1:
            i1 = i
            break
    ok0, ops0 = False, []
    if i1 > -1:
        ok0 = True
        for i, a in enumerate(A):
            if i % 2 == 0 and a % 2 == 1: ops0.append((i+1, i1+1))
            if i % 2 == 1 and a % 2 == 0: ops0.append((i+1, i1+1))    

    # 1 first
    i1 = -1
    for i in range(0, N, 2):
        if A[i] % 2 == 1:
            i1 = i
            break
    ok1, ops1 = False, []
    if i1 > -1:
        ok1 = True
        for i, a in enumerate(A):
            if i % 2 == 0 and a % 2 == 0: ops1.append((i+1, i1+1))
            if i % 2 == 1 and a % 2 == 1: ops1.append((i+1, i1+1))  

    if not ok0 and not ok1: return -1, []
    if ok0 and (not ok1 or len(ops0) < len(ops1)): return len(ops0), ops0
    return len(ops1), ops1


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        out1, out2 = solve(N, A)
        print(out1)
        for tup in out2: print(*tup)


if __name__ == '__main__':
    main()

