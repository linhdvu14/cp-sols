''' B. Equalize by Divide
https://codeforces.com/contest/1799/problem/B
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

def solve(N, A):
    if len(set(A)) == 1: return 0, []
    if 1 in A: return -1, []

    res = []
    while len(set(A)) != 1:
        for i in range(N):
            for j in range(i):
                while A[i] != A[j]:
                    if A[i] > A[j]:
                        res.append([i + 1, j + 1])
                        A[i] = (A[i] + A[j] - 1) // A[j]
                    else:
                        res.append([j + 1, i + 1])
                        A[j] = (A[j] + A[i] - 1) // A[i]

    return len(res), res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        a, b = solve(N, A)
        print(a)
        for t in b: print(*t)


if __name__ == '__main__':
    main()

