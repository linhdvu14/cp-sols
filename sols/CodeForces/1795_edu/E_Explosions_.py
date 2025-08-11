''' E. Explosions?
https://codeforces.com/contest/1795/problem/E
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
    # L[i] = area under left downslope if peak is A[i]
    L = [0] * (N + 1)
    st = []
    for i, a in enumerate(A):
        # rightmost j s.t. A[j] <= A[i] - (i - j)
        while st and st[-1][0] > a - i: st.pop()
        j = st[-1][1] if st else -1
        b = max(a - (i - j - 1), 0)
        L[i] = (a + b) * (a - b + 1) // 2 + L[j]
        st.append([a - i, i])

    # R[i] = area under right downslope if peak is A[i]
    R = [0] * (N + 1)
    st = []
    for i in range(N - 1, -1, -1):
        a = A[i]
        # leftmost j s.t. A[j] <= A[i] - (j - i)
        while st and st[-1][0] > a + i: st.pop()
        j = st[-1][1] if st else N 
        b = max(0, a - (j - i - 1))
        R[i] = (a + b) * (a - b + 1) // 2 + R[j]
        st.append([a + i, i])

    res = S = sum(A)
    for i, a in enumerate(A):
        save = L[i] + R[i] - a
        res = min(res, S - save + a)

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        res = solve(N, A)
        print(res)


if __name__ == '__main__':
    main()

