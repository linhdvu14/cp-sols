''' Array Partition
https://www.codechef.com/JAN222A/problems/ARRPART
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug')

if DEBUG:
    from inspect import currentframe, getframeinfo
    from re import search

def debug(*args):
    if not DEBUG: return
    frame = currentframe().f_back
    s = getframeinfo(frame).code_context[0]
    r = search(r"\((.*)\)", s).group(1)
    vnames = r.split(', ')
    var_and_vals = [f'{var}={val}' for var, val in zip(vnames, args)]
    prefix = f'{currentframe().f_back.f_lineno:02d}: '
    print(f'{prefix}{", ".join(var_and_vals)}')


INF = float('inf')

# -----------------------------------------

MOD = 998244353
rev = []
roots = [0, 1]

POW_N = [-1] * (10**6 + 1)
POW_K = [-1] * 21

def dft(a):
    global rev
    n = len(a)
    if len(rev) != n:
        k = (n.bit_length()-1)-1
        rev += [0] * (n - len(rev))
        for i in range(n):
            rev[i] = (rev[i>>1]>>1) | ((i&1)<<k)
    for i in range(n):
        if rev[i] < i:
            a[i], a[rev[i]] = a[rev[i]], a[i]
    if len(roots) < n:
        k = len(roots).bit_length()-1
        roots.extend([0]*(n-len(roots)))
        while ((1<<k) < n):
            if POW_K[k] == -1: POW_K[k] = pow(3, (MOD-1)>>(k+1), MOD)
            e = POW_K[k]
            for i in range(1<<(k-1), 1<<k):
                roots[2*i] = roots[i]
                roots[2*i+1] = (roots[i]*e) % MOD
            k += 1
    k = 1
    while k < n:
        i = 0
        while i < n:
            for j in range(k):
                u = a[i+j]
                v = (a[i+j+k]*roots[k+j]) % MOD
                a[i+j] = (u+v) % MOD
                a[i+j+k] = (u-v) % MOD
            i += 2*k
        k *= 2
 
def idft(a):
    n = len(a)
    a[1:] = a[1:][::-1]
    dft(a)
    if POW_N[n] == -1: POW_N[n] = pow(n, MOD-2, MOD)
    inv = POW_N[n]
    for i in range(n):
        a[i] = (a[i]*inv) % MOD
 
def convmod(a, b):
    if not a or not b:
        return []
    sz, tot = 1, len(a)+len(b)-1
    while sz < tot:
        sz *= 2
    a.extend([0]*(sz-len(a)))
    b.extend([0]*(sz-len(b)))
    dft(a)
    dft(b)
    for i in range(sz):
        a[i] = (a[i]*b[i]) % MOD
    idft(a)
    return a[:tot]

from collections import deque

def solve(N, X, A):
    # A = [1 if a >= X else 0 for a in A]
    # want to partition A into k subarrays s.t. each subarray contains at least 1 one
    # B = num zeroes between adjacent ones, plus 1
    global rev
    rev = []
    B = []
    cnt = 1
    for a in A:
        if a >= X:
            B.append(cnt)
            cnt = 1
        else:
            cnt += 1
    
    if len(B) == 0: 
        print(*[0]*N)
        return
    if len(B) == 1: 
        print(*[1] + [0]*(N-1))
        return
    
    B = B[1:]

    # say A has 5 ones, B = [a, b, c, d]
    # k > 5: res = 0
    # k = 5: res = abcd  (each one in own partition, a ways to separate 1st and 2nd ones, b ways to separate 2nd and 3rd ones, etc.)
    # k = 4: res = abc + abd + bcd (bcd = num ways to partition if merge 1st and 2nd ones, etc.)
    # k = 3: res = ab + ac + ad + bc + bd + cd
    # k = 2: res = a + b + c + d
    # k = 1: res = 1
    
    # let P = (1 + ax) (1 + bx) (1 + cx) (1 + dx)
    # then P = 1 + (a + b + c + d) x + (ab + ac + ad + bc + bd + cd) x^2 + (abc + abd + bcd) x^3 + (abcd) x^4
    # has coefficients [res(k) for k=1..5]

    queue = deque([[1, b] for b in B])
    while len(queue) > 1:
        a = queue.popleft()
        b = queue.popleft()
        a = convmod(a, b)
        queue.append(a)

    res = queue.pop()
    res += [0]*(N-len(res))
    print(*res)


def main():
    T = int(input())
    for _ in range(T):
        N, X = list(map(int, input().split()))
        A = list(map(int, input().split()))
        solve(N, X, A)


if __name__ == '__main__':
    main()

