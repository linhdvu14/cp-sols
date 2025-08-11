''' Problem A: On the Run
https://www.facebook.com/codingcompetitions/hacker-cup/2019/round-2/problems/A
'''

# cannot win with 1 agent
# can only win immediately if dist(x, a) == dist(x, b) == 1, else X always has a move
# da, db % 2 do not change change
# can always decrease at least da or db in one turn, with one agent reducing X-distance and the other reducing Y-distance

def solve(M,N,x,agents):
    if len(agents) == 1: return 'N'
    x1, x2 = x
    a1, a2 = agents[0]
    b1, b2 = agents[1]
    d1, d2 = (abs(a1-x1) + abs(a2-x2)) % 2, (abs(b1-x1) + abs(b2-x2)) % 2
    return 'Y' if d1 % 2 == 0 and d2 % 2 ==0 else 'N'

def main():
    from sys import stdin
    
    T = int(stdin.readline().strip())
    for t in range(T):
        M, N, K = list(map(int, stdin.readline().strip().split()))
        x = tuple(map(int, stdin.readline().strip().split()))
        agents = [tuple(map(int, stdin.readline().strip().split())) for _ in range(K)]
        out = solve(M,N,x,agents)
        print('Case #{}: {}'.format(t+1, out))


if __name__ == '__main__':
    main()
