''' C. No Prime Differences
https://codeforces.com/contest/1838/problem/C
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

def sieve(N):
    prime = [1] * (N + 1)
    prime[0] = prime[1] = 0
    for i in range(2, N + 1):
        if i * i > N: break 
        if not prime[i]: continue
        for j in range(i * 2, N + 1, i): prime[j] = 0
    return prime

PRIME = sieve(1000)


def solve(R, C):
    res = [[0] * C for _ in range(R)]

    if not PRIME[C]:
        for r in range(R):
            for c in range(C):
                res[r][c] = r * C + c + 1
    elif not PRIME[R]:
        for r in range(R):
            for c in range(C):
                res[r][c] = c * R + r + 1
    else:
        for r in range(R):
            offset = r % C 
            for c in range(C):
                res[r][(c - offset) % C] = r * C + c + 1

    return res


def main():
    T = int(input())
    for _ in range(T):
        R, C = list(map(int, input().split()))
        res = solve(R, C)
        for r in res: print(*r)
        print()


if __name__ == '__main__':
    main()

