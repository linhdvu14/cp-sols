''' B. Three Sevens
https://codeforces.com/contest/1798/problem/B
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
    res = [-1] * N 
    bad = set()
    for i in range(N - 1, -1, -1):
        for a in A[i]:
            if a not in bad: 
                res[i] = a 
                break
        else:
            return [-1]
        bad |= set(A[i])

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = []
        for _ in range(N):
            _ = input()
            A.append(list(map(int, input().split())))
        res = solve(N, A)
        print(*res)


if __name__ == '__main__':
    main()

