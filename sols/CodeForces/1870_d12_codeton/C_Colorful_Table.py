''' C. Colorful Table
https://codeforces.com/contest/1870/problem/C
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

def solve(N, K, A):
    first, last = [INF] * K, [-INF] * K
    for i, a in enumerate(A):
        if first[a - 1] is INF: first[a - 1] = i
        last[a - 1] = i

    # L[k] = leftmost i s.t. A[i] == k
    L, R = [INF] * (K + 1), [-INF] * (K + 1)
    for i in range(K - 1, -1, -1):
        L[i] = min(L[i + 1], first[i])
        R[i] = max(R[i + 1], last[i])

    res = []
    for i in range(K):
        if first[i] is INF: res.append(0)
        else: res.append((R[i] - L[i] + 1) * 2)

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        A = list(map(int, input().split()))
        res = solve(N, K, A)
        print(*res)


if __name__ == '__main__':
    main()

