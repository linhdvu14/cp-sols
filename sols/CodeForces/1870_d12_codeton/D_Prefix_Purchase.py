''' D. Prefix Purchase
https://codeforces.com/contest/1870/problem/D
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

def solve(N, C, K):
    pos = {}
    for i, c in enumerate(C): pos[c] = max(pos.get(c, 0), i)

    choices = []
    for c in sorted(pos.keys()):
        if not choices or choices[-1][0] < pos[c]: 
            choices.append((pos[c], c))

    steps = []
    pc, pn = 0, INF
    for i, c in choices:
        n = min(K // (c - pc), pn)
        K -= n * (c - pc)
        if n: 
            steps.append((i, n))
            pc, pn = c, n

    res = [0] * N 
    i = 0
    for j, n in steps:
        while i <= j: 
            res[i] = n
            i += 1

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        C = list(map(int, input().split()))
        K = int(input())
        res = solve(N, C, K)
        print(*res)



if __name__ == '__main__':
    main()

