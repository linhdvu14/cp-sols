''' B. Serval and Inversion Magic
https://codeforces.com/contest/1789/problem/B
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
    i = 0
    while i < N // 2 and S[i] == S[-1 - i]: i += 1
    while i < N // 2 and S[i] != S[-1 - i]: i += 1
    while i < N // 2:
        if S[i] != S[-1 - i]: return 'No'
        i += 1
    
    return 'Yes'


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = input().decode().strip()
        res = solve(N, S)
        print(res)


if __name__ == '__main__':
    main()

