''' A2. Alternating Deck (hard version)
https://codeforces.com/contest/1786/problem/A2
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

def solve(N):
    res = [[0, 0], [0, 0]]
    i, j, s = 0, 0, 1
    while N: 
        use = min(s, N)
        res[i][j] += (use + 1) // 2
        res[i][j ^ 1] += use - (use + 1) // 2
        N -= use 
        s += 4
        i ^= 1
        j ^= 1

    return res[0] + res[1]


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        res = solve(N)
        print(*res)


if __name__ == '__main__':
    main()

