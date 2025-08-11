''' D. Binary Spiders
https://codeforces.com/contest/1625/problem/D
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

BITS = 30
 
class TrieNode:
    def __init__(self):
        self.child = [None, None]
        self.val = 0


# choose max set of numbers s.t. min xor over all consecutive pairs (after sorting) >= K
# dp[i] = max set size if max ele is A[i] -> O(N^2)

def solve_mle():
    N, K = list(map(int, input().split()))
    
    A = list(map(int, input().split()))
    A = [(a, i) for i, a in enumerate(A)]
    A.sort()

    # dp[i] = max size subset where max ele is A[i]
    dp = [1] * N
 
    # trie
    root = TrieNode()
    for i, (a, _) in enumerate(A):
        # descend into a^K to find max size subset
        cur = root
        for j in range(BITS-1, -1, -1):
            d = (a >> j) & 1
            if (K >> j) & 1 == 0:  # XOR bit != K bit, XOR > K
                if cur.child[d^1] is not None:
                    dp[i] = max(dp[i], cur.child[d^1].val)
                cur = cur.child[d]
            else:                  # XOR bit == K bit
                cur = cur.child[d^1]
            if not cur: break
        if cur: dp[i] = max(dp[i], cur.val)
 
        # descend into a to insert
        v = dp[i] + 1
        cur = root
        for j in range(BITS-1, -1, -1):
            d = (a >> j) & 1
            if cur.child[d] is None: cur.child[d] = TrieNode()
            cur = cur.child[d]
            cur.val = max(cur.val, v)

    # trace
    mxi = mxv = -1
    for i, v in enumerate(dp):
        if v > mxv: mxi, mxv = i, v
    
    if mxv <= 1: return [-1]

    idx = []
    v = mxv
    for i in range(mxi, -1, -1):
        if dp[i] == v:
            idx.append(A[i][1])
            v -= 1
    
    return idx


# https://codeforces.com/blog/entry/99031?#comment-879817
# https://codeforces.com/contest/1625/submission/142517827

# iterate over bit pos i from high to low
# divide arr into 2 sets: i-th bit equals 0 and i-th bit equals 1
# if i-th bit of K is 0, can recursively solve each set and combine
# if i-th bit of K is 1, can choose at most 1 ele from each set
# will recurse from highest bit till msb of K

def solve_ac():
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    if K == 0: return list(range(N))

    def solve_sub(idx, b):
        if not idx: return []
        left, right = [], []
        for i in idx:
            if (A[i] >> b) & 1 == 0: left.append(i)
            else: right.append(i)

        if (K >> b) & 1 == 0: return solve_sub(left, b-1) + solve_sub(right, b-1)
        if not left: return [right[0]]
        if not right: return [left[0]]
        if b == 0: return [left[0], right[0]]

        root = TrieNode()
        
        # add all left eles
        for i in left: 
            cur = root
            for j in range(b-1, -1, -1):
                d = (A[i] >> j) & 1
                if cur.child[d] is None: cur.child[d] = TrieNode()
                cur = cur.child[d]
        
        # check if any (left, right) pair has XOR >= K
        for i in right:
            ok = False
            cur = root
            for j in range(b-1, -1, -1):
                d = (A[i] >> j) & 1
                if (K >> j) & 1 == 0:
                    if cur.child[d^1] is not None: ok = True
                    cur = cur.child[d]
                else:
                    cur = cur.child[d^1]
                if ok or cur is None: break
            if cur: ok = True
            
            if ok:
                for j in left:
                    if A[i] ^ A[j] >= K:
                        return [i, j]

        return [left[0]]

    res = solve_sub(list(range(N)), 29)
    return res


solve = solve_ac


if __name__ == '__main__':
    out = solve()
    if len(out) < 2:
        print(-1)
    else:
        print(len(out))
        print(*[i+1 for i in out])
 