''' E. William The Oblivious
https://codeforces.com/contest/1609/problem/E
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

INF = float('inf')

class Node:
    def __init__(self, lo, hi):
        self.lo = lo
        self.hi = hi
        self.mi = (lo+hi) // 2
        self.left = None
        self.right = None

        # dp[i][j] = min cost s.t. no subseq i..j
        # dp[0][2] = min cost s.t. no subseq 'abc'
        self.dp = [[0]*3 for _ in range(3)]

    def _update_from_child(self):
        '''update par val after updating children vals. CHANGE HERE'''
        # min cost of no 'abc' = min of
        # * no 'abc' in left, no 'c' in right
        # * no 'ab' in left, no 'bc' in right
        # * no 'a' in left, no 'abc' in right
        for i in range(3):
            for j in range(i, 3):
                self.dp[i][j] = INF
                for k in range(i, j+1):
                    l = self.left.dp[i][k] if self.left else 0
                    r = self.right.dp[k][j] if self.right else 0
                    self.dp[i][j] = min(self.dp[i][j], l + r)


    def update(self, qi, c):
        '''update all segments s.t. S[qi]=c'''
        if qi < self.lo or qi > self.hi: return
        if qi == self.lo == self.hi:
            self.dp = [[0]*3 for _ in range(3)]
            self.dp[ord(c)-ord('a')][ord(c)-ord('a')] = 1
        else:
            if qi <= self.mi: self.left.update(qi, c)
            else: self.right.update(qi, c)
            self._update_from_child()


class SegmentTree:
    def __init__(self, S):
        def construct(lo, hi):
            '''construct st on S[lo..hi]'''
            if lo > hi: return None
            root = Node(lo, hi)
            if lo == hi:
                root.dp[ord(S[lo])-ord('a')][ord(S[lo])-ord('a')] = 1
            else:
                mi = (lo+hi) // 2
                root.left = construct(lo, mi)
                root.right = construct(mi+1, hi)
                root._update_from_child()
            return root        
        self.root = construct(0, len(S)-1)
    
    def update(self, qi, c):
        '''update S[qi]=c'''
        self.root.update(qi, c)


# https://codeforces.com/blog/entry/97350?#comment-862540
def solve(N, Q, S, queries):
    st = SegmentTree(S)
    for i, c in queries:
        st.update(i, c)
        print(st.root.dp[0][2])


def main():
    N, Q = list(map(int, input().split()))
    S = input().decode().strip()
    queries = []
    for _ in range(Q):
        ts = input().decode().strip().split()
        queries.append((int(ts[0])-1, ts[1]))
    solve(N, Q, S, queries)


if __name__ == '__main__':
    main()

