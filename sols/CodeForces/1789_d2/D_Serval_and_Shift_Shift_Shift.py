''' D. Serval and Shift-Shift-Shift
https://codeforces.com/contest/1789/problem/D
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
    if A == B: return 0, []
    if (A != 0) ^ (B != 0): return -1, []

    res = 0
    ONE = (1 << N) - 1
    def shift(k):
        if not k: return
        res.append(k)
        nonlocal A 
        if k > 0: A ^= (A << k) & ONE
        else: A ^= (A >> (-k)) & ONE

    ha = hb = -1
    for i in range(N):
        if (A >> i) & 1: ha = i 
        if (B >> i) & 1: hb = i

    res = []
    if ha <= hb:
        shift(hb - ha)
        for i in range(hb - 1, -1, -1):
            if (A >> i) & 1 != (B >> i) & 1:
                shift(i - hb)
    else:
        for i in range(ha - 1, -1, -1):
            if (A >> i) & 1 != (B >> i) & 1:
                shift(i - ha)
        for la in range(N):
            if (A >> la) & 1: break 
        for i in range(ha, N):
            if (A >> i) & 1:
                shift(i - la)

    return len(res), res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = int(input().decode().strip(), 2)
        B = int(input().decode().strip(), 2)
        a, b = solve(N, A, B)
        print(a)
        if b: print(*b)

if __name__ == '__main__':
    main()
