''' B - Light It Up
https://atcoder.jp/contests/abc255/tasks/abc255_b
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

def main():
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    pts = [list(map(int, input().split())) for _ in range(N)]

    dist = [INF] * N
    for i in range(N):
        for j in A:
            j -= 1
            dist[i] = min(dist[i], (pts[i][0] - pts[j][0])**2 + (pts[i][1] - pts[j][1])**2)
    
    print(max(dist)**0.5)



if __name__ == '__main__':
    main()

