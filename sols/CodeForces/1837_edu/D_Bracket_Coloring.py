''' D. Bracket Coloring
https://codeforces.com/contest/1837/problem/D
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

def solve(N, S):
    L, R = [], []
    for i, c in enumerate(S):
        if c == '(': L.append(i)
        else: R.append(i)
    
    if len(L) != len(R): return -1, []

    res = [-1] * N
    for l, r in zip(L, R):
        if l > r: res[l] = res[r] = 1
        else: res[l] = res[r] = 2
    
    if len(set(res)) == 1: return 1, [1] * N
    return 2, res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = input().decode().strip()
        a, b = solve(N, S)
        print(a)
        if b: print(*b)

if __name__ == '__main__':
    main()

