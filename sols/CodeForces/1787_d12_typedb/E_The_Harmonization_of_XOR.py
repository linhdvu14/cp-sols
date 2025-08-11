''' E. The Harmonization of XOR
https://codeforces.com/contest/1787/problem/E
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

# if have m vals y in 1..n with bit msb(x) set
# - k <= m
# - x^y also in 1..n
# - parity(xor(1..n)) = parity(m) ^ parity(remain)

def solve(N, K, X):
    msb = -1
    for i in range(29, -1, -1):
        if (X >> i) & 1:
            msb = i
            break
    
    use = [0] * (N + 1)
    res, rem = [], []
    rem_xor = 0
    for a in range(N + 1):
        if use[a]: continue
        if (a >> msb) & 1 == 0 and a ^ X <= N:
            if a: res.append([a, a ^ X])
            else: res.append([X])
            use[a] = use[a ^ X] = 1
        elif a:
            rem.append(a)
            rem_xor ^= a 

    if len(res) < K: return 'NO', []
    if X * (len(res) & 1) ^ rem_xor != X * (K & 1): return 'NO', []
    
    res[0] += rem
    while len(res) > K: res[0] += res.pop()

    return 'YES', res


def check(N, K, X, res):
    if not res: return
    assert len(res) == K

    vals = []
    for s in res:
        xor = 0 
        for a in s:
            vals.append(a)
            xor ^= a
        assert s and xor == X, f's={s} xor={xor} X={X}'
    
    vals.sort()
    assert vals == list(range(1, N + 1)), vals


def main():
    T = int(input())
    for _ in range(T):
        N, K, X = list(map(int, input().split()))
        a, b = solve(N, K, X)
        print(a)
        for t in b: print(len(t), *t)
        check(N, K, X, b)


if __name__ == '__main__':
    main()

