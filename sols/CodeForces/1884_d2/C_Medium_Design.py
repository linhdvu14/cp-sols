''' C. Medium Design
https://codeforces.com/contest/1884/problem/C 
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

def solve(N, M, segs):
    def max_cover(segs):
        pts = []
        for l, r in segs: pts += [[l, 1], [r + 1, -1]]
        pts.sort()

        res = cnt = 0
        for _, a in pts:
            cnt += a
            res = max(res, cnt)

        return res
    
    res = max(
        max_cover([s for s in segs if s[0] != 1]),
        max_cover([s for s in segs if s[-1] != M]),
    )

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))
        segs = [list(map(int, input().split())) for _ in range(N)]
        res = solve(N, M, segs)
        print(res)


if __name__ == '__main__':
    main()

