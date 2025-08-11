''' Cherries Mesh 
https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050edb/0000000000170721
'''
class UnionFind:
    def __init__(self, n):
        self.size = [1 for _ in range(n)]
        self.parent = [i for i in range(n)]
    
    def find(self, i):
        while self.parent[i] != self.parent[self.parent[i]]:
            self.parent[i] = self.parent[self.parent[i]]
        return self.parent[i]

    def union(self, i, j):
        rooti, rootj = self.find(i), self.find(j)
        if rooti == rootj:
            return
        if self.size[rooti] > self.size[rootj]:
            rooti, rootj = rootj, rooti
        self.parent[rooti] = rootj
        self.size[rootj] += self.size[rooti]
    
    def get_size(self, i):
        return self.size[self.find(i)]


def solve(uf, n):
    if n == 1: return 0
    return n-2 + len(set(uf.find(i) for i in range(n)))


def main():
    from sys import stdin

    T = int(stdin.readline().strip())
    for t in range(T):
        n, m = list(map(int, stdin.readline().strip().split()))
        uf = UnionFind(n)

        for _ in range(m):
            c, d = list(map(int, stdin.readline().strip().split()))
            uf.union(c-1, d-1)

        out = solve(uf, n)
        print('Case #{}: {}'.format(t+1, out))


if __name__ == '__main__':
    main()