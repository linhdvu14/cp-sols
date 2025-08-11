''' G. Another Wine Tasting Event
https://codeforces.com/contest/1776/problem/G
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

# extended segments on left have endpoints (R, W)
# extended segmets on right have endpoints (W, R)
def solve(N, S):
    cnt = 0
    for i in range(N):
        if S[i] == 'W': cnt += 1
    
    mx = cnt 
    for i in range(N, 2 * N - 1):
        if S[i] == 'W': cnt += 1
        if S[i - N] == 'W': cnt -= 1
        mx = max(mx, cnt)

    return mx


def main():
    N = int(input())
    S = input().decode().strip()
    res = solve(N, S)
    print(res)


if __name__ == '__main__':
    main()
