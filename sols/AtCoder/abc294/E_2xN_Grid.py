''' E - 2xN Grid
https://atcoder.jp/contests/abc294/tasks/abc294_e
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
    L, N1, N2 = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(N1)][::-1]
    B = [list(map(int, input().split())) for _ in range(N2)][::-1]
    
    res = l = 0
    v1, r1 = A.pop()
    v2, r2 = B.pop()
    while True:
        if v1 == v2: res += min(r1, r2) - l 
        if not A and not B: break 
        if r1 <= r2:
            v1, cnt = A.pop()
            l = r1
            r1 += cnt 
        else:
            v2, cnt = B.pop()
            l = r2
            r2 += cnt

    return res


if __name__ == '__main__':
    res = main()
    print(res)

