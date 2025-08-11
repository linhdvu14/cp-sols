''' Problem D2: Work-Life Balance - Chapter 2
https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-2/problems/D2
'''

import os, sys
input = sys.stdin.readline
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

class FenwickTree:
    '''basic 0-base sum Fenwick tree for point update, range query'''
    def __init__(self, data):
        '''transform list into BIT'''
        self.val = data[:]
        for i in range(len(self.val)):
            j = i | (i + 1)
            if j < len(self.val):
                self.val[j] += self.val[i]
    
    def add(self, i, x):
        '''point update data[i] += x'''
        while i < len(self.val):
            self.val[i] += x
            i |= i + 1   # 101 -> 110
    
    def query(self, i):
        '''prefix sum data[0..i]'''
        s = 0
        end = i + 1
        while end:
            s += self.val[end - 1]
            end &= end - 1  # 110 -> 100
        return s

    def query_range(self, l, r):
        '''range sum data[l..r]'''
        return self.query(r) - self.query(l-1)


MAX = 10**6 + 2

def solve(N, M, A, queries):
    fw_cnt = [None, FenwickTree([0] * MAX), FenwickTree([0] * MAX)]
    fw_pos = [None, FenwickTree([0] * MAX), FenwickTree([0] * MAX)]
    for i, a in enumerate(A): 
        fw_cnt[a].add(i, 1)
        fw_pos[a].add(i, i)
    
    # sum k leftmost positions of fw[a] in range l..r
    def sum_left(a, l, r, k):
        idx, lo, hi = -1, l, r 
        while lo <= hi:
            mi = (lo + hi) // 2
            if fw_cnt[a].query_range(l, mi) >= k:
                idx = mi 
                hi = mi - 1
            else:
                lo = mi + 1
        return fw_pos[a].query_range(l, idx)
    
    def sum_right(a, l, r, k):
        idx, lo, hi = -1, l, r 
        while lo <= hi:
            mi = (lo + hi) // 2
            if fw_cnt[a].query_range(mi, r) >= k:
                idx = mi
                lo = mi + 1
            else:
                hi = mi - 1
        return fw_pos[a].query_range(idx, r)
    
    def calc(n):
        cl = [0] * 3
        cr = [0] * 3
        sl = sr = 0
        for a in range(1, 3):
            cl[a] = fw_cnt[a].query_range(0, n - 1)
            cr[a] = fw_cnt[a].query_range(n, N - 1)
            sl += cl[a] * a 
            sr += cr[a] * a
 
        if (sl - sr) % 2: return -1
        if sl == sr: return 0

        # swap k rightmost 1s from left side with k leftmost 2s from right side
        if sl < sr:
            k = (sr - sl) // 2
            if cl[1] < k or cr[2] < k: return -1
            return sum_left(2, n, N - 1, k) - sum_right(1, 0, n - 1, k)
        
        k = (sl - sr) // 2
        if cl[2] < k or cr[1] < k: return -1
        return sum_left(1, n, N - 1, k) - sum_right(2, 0, n - 1, k)

    res = 0
    for i, v, n in queries:
        i -= 1
        if v != A[i]:
            fw_cnt[A[i]].add(i, -1)
            fw_pos[A[i]].add(i, -i)
            A[i] = v 
            fw_cnt[A[i]].add(i, 1)
            fw_pos[A[i]].add(i, i)
        res += calc(n)

    return res


def main():
    T = int(input())
    for t in range(T):
        N, M = list(map(int, input().split()))
        A = list(map(int, input().split()))
        queries = [list(map(int, input().split())) for _ in range(M)]
        res = solve(N, M, A, queries)
        print(f'Case #{t+1}: {res}')


if __name__ == '__main__':
    main()

