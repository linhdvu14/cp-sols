''' D. Binary String Sorting
https://codeforces.com/contest/1809/problem/D
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

COST = 10**12

def solve(S):
    zero = S.count('0')
    one = 0

    res = min(zero, len(S) - zero) * (COST + 1)
    for i, c in enumerate(S):
        if c == '0': zero -= 1
        else: one += 1
        cand = (one + zero) * (COST + 1)
        if S[i:i + 2] == '10': cand = min(cand, COST + (one + zero - 2) * (COST + 1))
        res = min(res, cand)
            
    return res


def main():
    T = int(input())
    for _ in range(T):
        S = input().decode().strip()
        res = solve(S)
        print(res)


if __name__ == '__main__':
    main()

