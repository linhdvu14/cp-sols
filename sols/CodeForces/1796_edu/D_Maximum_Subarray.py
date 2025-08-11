''' D. Maximum Subarray
https://codeforces.com/contest/1796/problem/D
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

class SparseTableMin:
    def __init__(self, data, func=min):
        self.func = func
        self.data = [list(data)]
        d, n = 1, len(data)
        while 2 * d <= n:
            cur = self.data[-1]
            nxt = [func(cur[i], cur[i + d]) for i in range(n - 2 * d + 1)]
            self.data.append(nxt)
            d <<= 1

    def query(self, l, r):
        '''func of data[l..r]; O(1)'''
        d = (r - l + 1).bit_length() - 1
        return self.func(self.data[d][l], self.data[d][r - (1 << d) + 1])


def solve(N, K, X, A):
    for i in range(N): A[i] -= X 
    X *= 2

    psum = [0] * (N + 1)
    for i, a in enumerate(A): psum[i + 1] = psum[i] + a
    st = SparseTableMin(psum)

    res = 0
    if X >= 0:
        for i in range(N):
            for k in range(min(i + 1, K) + 1): res = max(res, psum[i + 1] - psum[i - k + 1] + k * X)
            if i >= K: res = max(res, psum[i + 1] - st.query(0, i - K) + K * X)
    else:
        for i in range(N):
            rem = max(K - (N - 1 - i), 0)
            for k in range(min(i + 1, rem) + 1): res = max(res, psum[i + 1] - psum[k] + (rem - k) * X)
            if rem <= i: res = max(res, psum[i + 1] - st.query(rem, i))

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, K, X = list(map(int, input().split()))
        A = list(map(int, input().split()))
        res = solve(N, K, X, A)
        print(res)


if __name__ == '__main__':
    main()
