''' E. Guess Game
https://codeforces.com/contest/1864/problem/E
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
MOD = 998244353
BITS = 30

class Trie:
    def __init__(self, max_adds):
        n = min(max_adds * BITS, 1 << (BITS + 1))     # num trie nodes
        self.nodes = [0] * (2 * n)  # nodes[2*parID] = child0ID, nodes[2*parID+1] = child1ID, 0 if no child
        self.cnt = [0] * (n + 1)    # count eles under this node ID
        self.id = 0                 # index into free slots
    
    def add(self, x):
        '''add 1 count of x to trie'''
        v = 0
        stack = [v]
        for i in range(BITS - 1, -1, -1):
            c = (x >> i) & 1
            if self.nodes[2 * v + c] == 0:
                self.id += 1
                self.nodes[2 * v + c] = self.id
            v = self.nodes[2 * v + c]
            stack.append(v)
        for v in stack:
            self.cnt[v] += 1

    def query(self, x):
        '''total turns over all b if a = x'''
        v = 0
        res = one = 0
        for j in range(BITS - 1, -1, -1):
            c = (x >> j) & 1
            one += 1

            # b have opposite bit
            ways = one + (one & 1) if c else one + (one & 1 ^ 1)
            c2 = self.nodes[2 * v + (c ^ 1)]
            dup = self.cnt[c2] if c2 else 0
            res += ways * dup
            v = self.nodes[2 * v + c]
            
            if not c: one -= 1
        
        # b == a
        res += (bin(x).count('1') + 1) * self.cnt[v]

        return res


def solve(N, A):
    trie = Trie(N)
    for a in A: trie.add(a)

    res = 0
    for a in A:
        res = (res + trie.query(a)) % MOD

    return res * pow(N * N, MOD - 2, MOD) % MOD


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        res = solve(N, A)
        print(res)


def f(a, b):
    pos = [p for p in range(BITS - 1, -1, -1) if ((a | b) >> p) & 1]
    if not pos: return 1
    if (a >> pos[0]) & 1 == 0: return 1

    res = 1
    for i, p in enumerate(pos):
        res += 1
        if (b >> p) & 1 == 0: break
        if i + 1 == len(pos) or (b >> pos[i + 1]) & 1 == 0: break 
        a, b = b, a

    return res


if __name__ == '__main__':
    main()

