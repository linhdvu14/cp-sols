''' D. Andrey and Escape from Capygrad
https://codeforces.com/contest/1859/problem/D
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

def solve(N, segs, Q, queries):
    res = queries[:]

    segs.sort(key=lambda t: (t[3], t[1])) # inner right -> outer right
    idx = sorted(list(range(Q)), key=lambda i: queries[i])    
    
    while segs and idx:
        l, r, _, mx = segs.pop()
        while segs and max(segs[-1][2], l) <= min(segs[-1][3], r):
            l2, r2, _, _ = segs.pop()
            l = min(l, l2)
            r = max(r, r2)
        while idx and queries[idx[-1]] >= l:
            i = idx.pop()
            res[i] = max(queries[i], mx)

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        segs = [list(map(int, input().split())) for _ in range(N)]
        Q = int(input())
        queries = list(map(int, input().split()))
        res = solve(N, segs, Q, queries)
        print(*res)


if __name__ == '__main__':
    main()

