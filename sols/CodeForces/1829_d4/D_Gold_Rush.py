''' D. Gold Rush
https://codeforces.com/contest/1829/problem/D
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

def solve(N, M):
    if N == M: return 'YES'

    seen = {N}
    rem = [N]
    while rem:
        x = rem.pop()
        if x % 3: continue
        for y in [x // 3, x // 3 * 2]:
            if y in seen: continue
            if y == M: return 'YES'
            seen.add(y)
            rem.append(y)

    return 'NO'


def main():
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))
        res = solve(N, M)
        print(res)


if __name__ == '__main__':
    main()

