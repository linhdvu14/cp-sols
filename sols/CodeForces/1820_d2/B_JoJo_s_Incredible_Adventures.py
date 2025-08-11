''' B. JoJo's Incredible Adventures
https://codeforces.com/contest/1820/problem/B
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
    N = len(S)
    if '0' not in S: return N ** 2
    
    S *= 2
    M = len(S)

    res = i = 0
    while i < M:
        while i < M and S[i] == '0': i += 1
        j = i 
        while j < M and S[j] == '1': j += 1
        d = min(j - i, M) + 1
        res = max(res, (d // 2) * (d - d // 2))
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

