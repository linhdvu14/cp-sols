''' A. Channel
https://codeforces.com/contest/1863/problem/A
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

def solve(N, A, Q, S):
    if A == N: return 'YES'
    
    cur = tot = A
    for c in S:
        if c == '-': cur -= 1
        else: cur += 1; tot += 1
        if cur == N: return 'YES'
    
    if tot >= N: return 'MAYBE'
    return 'NO'


def main():
    T = int(input())
    for _ in range(T):
        N, A, Q = list(map(int, input().split()))
        S = input().decode().strip()
        res = solve(N, A, Q, S)
        print(res)


if __name__ == '__main__':
    main()

