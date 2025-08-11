''' C. Search in Parallel
https://codeforces.com/contest/1814/problem/C
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

# A = [a1, a2, ..., ak] and B = [b1, b2, ..., bl] s.t. k + l == N
# processing times are: s1, 2*s1, ..., k*s1, s2, 2*s2, ..., l*s2
# pick N smallest elements

# intuition:
# - shorter time to process i
# - shorter wait time for boxes behind i

def solve(N, S1, S2, R):
    A, B = [], []

    idx = list(range(N))
    idx.sort(key=lambda i: R[i], reverse=True)

    for i in idx:
        if (len(A) + 1) * S1 <= (len(B) + 1) * S2: A.append(i + 1)
        else: B.append(i + 1)

    return A, B


def main():
    T = int(input())
    for _ in range(T):
        N, S1, S2 = list(map(int, input().split()))
        R = list(map(int, input().split()))
        a, b = solve(N, S1, S2, R)
        print(len(a), *a)
        print(len(b), *b)


if __name__ == '__main__':
    main()

