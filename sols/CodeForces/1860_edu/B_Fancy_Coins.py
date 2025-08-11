''' B. Fancy Coins
https://codeforces.com/contest/1860/problem/B
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

def solve(M, K, a1, ak):
    if M // K < ak: return max(M - M // K * K - a1, 0)

    M -= ak * K    
    nk = max(M - a1, 0) // K
    res = nk + max(M - nk * K - a1, 0)
    if (nk + 1) * K <= M: res = min(res, nk + 1 + max(M - (nk + 1) * K - a1, 0))
    
    return res


def main():
    T = int(input())
    for _ in range(T):
        M, K, a1, ak = list(map(int, input().split()))
        res = solve(M, K, a1, ak)
        print(res)


if __name__ == '__main__':
    main()

