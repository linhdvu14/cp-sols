''' E. Tyler and Strings
https://codeforces.com/contest/1649/problem/E
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') not in [None, '0']

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
MAX = 200000

INV = [1, 1]
FACT = [1, 1]
INV_FACT = [1, 1]
for i in range(2, MAX+1): 
    INV.append(pow(i, MOD-2, MOD))
    FACT.append((FACT[-1] * i) % MOD)
    INV_FACT.append(pow(FACT[-1], MOD-2, MOD))


class FenwickTreeSum:
    def __init__(self, data):
        '''transform list into BIT'''
        self.tree = data
        for i in range(len(data)):
            j = i | (i + 1)
            if j < len(data):
                data[j] += data[i]

    def query(self, end):
        '''calc sum(bit[:end])'''
        x = 0
        while end:
            x += self.tree[end - 1]
            end &= end - 1  # 110 -> 100
        return x

    def update(self, idx, x):
        '''updates bit[idx] += x'''
        while idx < len(self.tree):
            self.tree[idx] += x
            idx |= idx + 1   # 101 -> 110


def solve(N, M, S, T):
    count = [0] * (MAX+1)
    for n in S: count[n] += 1
    fen = FenwickTreeSum(count[:])
    
    # (c1 + c2 + ... + cn)! / (c1! c2! ... cn!)
    X = FACT[N]
    for c in count:
        if c > 0:
            X = (X * INV_FACT[c]) % MOD

    res = 0
    for c in T:
        # i-th char of S strictly smaller than c
        res = (res + fen.query(c) * X * INV[N]) % MOD

        # i-th char of S equals c
        if count[c] == 0: 
            if N == 0: res += 1
            break
        
        X = (X * INV[N] * count[c]) % MOD
        fen.update(c, -1)
        count[c] -= 1
        N -= 1

    return res % MOD


def main():
    N, M = list(map(int, input().split()))
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    out = solve(N, M, S, T)
    output(f'{out}\n')


if __name__ == '__main__':
    main()

