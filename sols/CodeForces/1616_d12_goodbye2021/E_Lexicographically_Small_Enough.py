''' E. Lexicographically Small Enough
https://codeforces.com/contest/1616/problem/E
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') is not None

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

class FenwickTreeSum:
    def __init__(self, N, nums=[]):
        '''
        N = num distinct values
        nums = init values (len=N), if any
        '''
        self.N = N
        self.tree = [0]*(N+1)
        for i, num in enumerate(nums):
            self.update(i+1, num)

    def query(self, i):
        '''sum first i numbers A[1..i]'''
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)  # 110 -> 100
        return s

    def update(self, i, val):
        '''update A[i] += val (1-based)'''
        while i <= self.N:
            self.tree[i] += val
            i += i & (-i)  # 101 -> 110


# decompose S into multiset of chars and their orig indices in S
# want to construct S' s.t. S'[:i] == T[:i] followed by S'[i] < T[i]

# build S' char by char
# for each position, pop a good char (c) with the lowest orig index (j) in multiset
# current index of c will be shifted right by how many indices > j that have been popped

def solve(N, S, T):
    S = [ord(c)-ord('a') for c in S]
    T = [ord(c)-ord('a') for c in T]

    avail = [[] for _ in range(26)]
    for i in range(N-1, -1, -1): avail[S[i]].append(i)

    # fw.query(i) = how many indices < i have been popped
    fw = FenwickTreeSum(N)

    res = INF
    pref = 0  # cost to make S[:i] == T[:i]
    for i, t in enumerate(T):
        # make S[i] < T[i]
        cur = INF  
        for c in range(t):
            if not avail[c]: continue
            j = avail[c][-1]
            d = fw.query(j)
            cur = min(cur, j - d)  # (j + (i - d)) - i
        
        res = min(res, pref + cur)
 
        # make S[:i+1] == T[:i+1]
        if not avail[t]: break
        j = avail[t].pop()
        d = fw.query(j)
        pref += j - d
        fw.update(j + 1, 1)

    return res if res < INF else -1


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = input().decode().strip()
        T = input().decode().strip()
        out = solve(N, S, T)
        output(f'{out}\n')


if __name__ == '__main__':
    main()
