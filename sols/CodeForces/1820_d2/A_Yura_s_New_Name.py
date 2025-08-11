''' A. Yura's New Name
https://codeforces.com/contest/1820/problem/A
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

def solve(S):
    res = 0
    if S[0] != '^': 
        S = '^' + S 
        res += 1
    if S[-1] != '^':
        S += '^'
        res += 1
    
    N = len(S)
    if N == 1: return 1

    i = 0
    while i < N:
        j = i 
        while j < N and S[j] == S[i]: j += 1
        if S[i] == '_': res += j - i - 1
        i = j

    return res


def main():
    T = int(input())
    for _ in range(T):
        S = input().decode().strip()
        res = solve(S)
        print(res)


if __name__ == '__main__':
    main()

