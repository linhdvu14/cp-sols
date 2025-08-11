''' D. Buying gifts
https://codeforces.com/contest/1802/problem/D
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

from bisect import bisect_left, bisect_right

def solve(N, pairs):
    B = sorted([b for _, b in pairs])
    pairs.sort()

    res = INF 
    mxb = -INF
    while pairs:
        mxa, b = pairs.pop()
        bs = [b]
        while pairs and pairs[-1][0] == mxa: bs.append(pairs.pop()[1])         

        i = bisect_left(B, mxa) 
        if len(bs) == 1 and i < N and B[i] == bs[0]: i += 1
        if i < N and B[i] >= mxb: res = min(res, B[i] - mxa)
        
        j = bisect_right(B, mxa) - 1
        if len(bs) == 1 and j >= 0 and B[j] == bs[0]: j -= 1
        if j >= 0 and B[j] >= mxb: res = min(res, mxa - B[j])

        res = min(res, abs(mxa - mxb))
        for b in bs: mxb = max(mxb, b)
    
    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        pairs = [list(map(int, input().split())) for _ in range(N)]
        res = solve(N, pairs)
        print(res)


if __name__ == '__main__':
    main()

