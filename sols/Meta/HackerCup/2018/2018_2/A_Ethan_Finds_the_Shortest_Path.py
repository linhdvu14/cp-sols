''' Problem A: Ethan Finds the Shortest Path
https://www.facebook.com/codingcompetitions/hacker-cup/2018/round-2/problems/A
'''

# Ethan's path must be monotonically decreasing: 
# 1 ___(K-1)___2___(K-2)___3___(K-3)___4___(K-4)___N
# for optimal path, connect 1___(K)___N

def solve(N, K):
    bad_weight = 0
    bad_edges = []
    src, w = 1, K-1
    while src+1<N and w>1:
        bad_weight += w
        bad_edges.append((src,src+1,w))
        src += 1
        w -= 1
    bad_weight += w
    bad_edges.append((src,N,w))    
    bad_edges.append((1,N,K))
    
    if bad_weight<K: return 0, [(1,N,1)]
    return bad_weight-K, bad_edges


def main():
    from sys import stdin
    
    T = int(stdin.readline().strip())
    for t in range(T):
        N, K = list(map(int, stdin.readline().strip().split()))
        out, edges = solve(N, K)
        print(f'Case #{t+1}: {out}')
        print(f'{len(edges)}')
        for u,v,w in edges: print(f'{u} {v} {w}')


if __name__ == '__main__':
    main()
