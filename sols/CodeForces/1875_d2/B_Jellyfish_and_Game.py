''' B. Jellyfish and Game
https://codeforces.com/contest/1875/problem/B
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

def solve(N, M, K, A, B):
    for i in range(min(K, 4 + K % 2)):
        if i % 2 == 0:
            A.sort(reverse=True)
            B.sort()
            if A[-1] < B[-1]:
                a, b = A.pop(), B.pop()
                A.append(b)
                B.append(a)
        else:
            B.sort(reverse=True)
            A.sort()
            if B[-1] < A[-1]:
                a, b = A.pop(), B.pop()
                A.append(b)
                B.append(a)

    return sum(A)


def main():
    T = int(input())
    for _ in range(T):
        N, M, K = list(map(int, input().split()))
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        res = solve(N, M, K, A, B)
        print(res)


if __name__ == '__main__':
    main()

