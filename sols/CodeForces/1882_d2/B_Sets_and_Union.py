''' B. Sets and Union
https://codeforces.com/contest/1882/problem/B
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

def solve(N, sets):
    res = 0
    for k in range(1, 51):
        ok = 0
        cand = set()
        for S in sets:
            if k in S: ok = 1; continue
            cand |= S
        if ok: res = max(res, len(cand))

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        sets = []
        for _ in range(N):
            S = list(map(int, input().split()))
            sets.append(set(S[1:]))
        res = solve(N, sets)
        print(res)


if __name__ == '__main__':
    main()

