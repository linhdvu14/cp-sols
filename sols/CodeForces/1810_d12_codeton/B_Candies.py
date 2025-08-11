''' B. Candies
https://codeforces.com/contest/1810/problem/B
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
    if N % 2 == 0: return -1, []
    
    res = []
    while N > 1:
        if (N + 1) // 2 % 2:
            res.append(1)
            N = (N + 1) // 2
        else:
            res.append(2)
            N = (N - 1) // 2

    return len(res), res[::-1]


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        a, b = solve(N)
        print(a)
        if b: print(*b)


if __name__ == '__main__':
    main()

