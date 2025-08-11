''' F2. Promising String (hard version)
https://codeforces.com/contest/1660/problem/F2
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

class FenwickTree:
    '''base-0 sum Fenwick tree'''
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


# if cnt(neg) - cnt(pos) >= 3, then there must be '--'
# changing '--' to '+' increases balance by 3
# interval i..j is promising if cnt(neg) >= cnt(pos) and (cnt(neg) - cnt(pos)) % 3 == 0
# i.e. bal = cnt(neg) - cnt(pos) >= 0 and bal % 3 == 0

def solve(N, S):
    res, bal = 0, N  # normalize bal 0 -> N
    trees = [FenwickTree([0]*(2*N+1)) for _ in range(3)]
    trees[bal % 3].update(bal, 1)
    for c in S:
        if c == '+': bal -= 1
        else: bal += 1
        res += trees[bal % 3].query(bal + 1)
        trees[bal % 3].update(bal, 1)
    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = input().decode().strip()
        out = solve(N, S)
        print(out)



if __name__ == '__main__':
    main()

