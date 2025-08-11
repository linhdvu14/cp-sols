''' G - Round Robin
https://atcoder.jp/contests/abc241/tasks/abc241_g
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

class Dinic:
    def __init__(self, n):
        '''init graph with n vertices'''
        self.lvl = [0] * n
        self.ptr = [0] * n
        self.q = [0] * n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, a, b, c, rc=0):
        '''add edge a -> b with capacity c and reverse capacity rc'''
        self.adj[a].append([b, len(self.adj[b]), c, 0])
        self.adj[b].append([a, len(self.adj[a]) - 1, rc, 0])

    def _dfs(self, v, t, f):
        if v == t or not f: return f
        for i in range(self.ptr[v], len(self.adj[v])):
            e = self.adj[v][i]
            if self.lvl[e[0]] == self.lvl[v] + 1:
                p = self._dfs(e[0], t, min(f, e[2] - e[3]))
                if p:
                    self.adj[v][i][3] += p
                    self.adj[e[0]][e[1]][3] -= p
                    return p
            self.ptr[v] += 1
        return 0

    def calc(self, s, t):
        '''return max flow from s to t'''
        flow, self.q[0] = 0, s
        for l in range(31):  # l = 30 maybe faster for random data
            while True:
                self.lvl, self.ptr = [0] * len(self.q), [0] * len(self.q)
                qi, qe, self.lvl[s] = 0, 1, 1
                while qi < qe and not self.lvl[t]:
                    v = self.q[qi]
                    qi += 1
                    for e in self.adj[v]:
                        if not self.lvl[e[0]] and (e[2] - e[3]) >> (30 - l):
                            self.q[qe] = e[0]
                            qe += 1
                            self.lvl[e[0]] = self.lvl[v] + 1

                p = self._dfs(s, t, INF)
                while p:
                    flow += p
                    p = self._dfs(s, t, INF)

                if not self.lvl[t]: break

        return flow



# check if each player p can be unique winner
# want to 
# * distribute N*(N-1)/2 wins to N*(N-1)/2 matches s.t. 1 win per match
# * each match distributes 1 win to either player; some wins are predefined
# * if player p receives w wins, all other players receive at most (w-1) wins
# * --> possible when max flow == total wins

def can_win(N, outcomes, p):
    # make p win all undetermined matches
    wins = N - 1 - sum(1 for _, l in outcomes if l == p)
    extra_outcomes = [(p, u) for u in range(N) if u != p and (u, p) not in outcomes]
    if wins == 0: return False

    # S -> A_uv -> B_u, B_v -> T
    L = N*N + N + 2
    network = Dinic(L)
    for u in range(N):
        bu = 1 + N*N + u
        for v in range(u):
            auv = 1 + u*N + v
            bv = 1 + N*N + v
            network.add_edge(0, auv, 1)
            if (v, u) not in outcomes and (v, u) not in extra_outcomes: network.add_edge(auv, bu, 1)
            if (u, v) not in outcomes and (u, v) not in extra_outcomes: network.add_edge(auv, bv, 1)
        if u == p: network.add_edge(1 + N*N + u, L - 1, wins)
        else: network.add_edge(1 + N*N + u, L - 1, wins - 1)

    # max flow
    flow = network.calc(0, L-1)
    return flow == N*(N-1) // 2
   

def main():
    N, M = list(map(int, input().split()))
    outcomes = set(tuple(map(int, input().split())) for _ in range(M))
    outcomes = [(w-1, l-1) for w, l in outcomes]
    winners = [u+1 for u in range(N) if can_win(N, outcomes, u)]
    print(*winners)



if __name__ == '__main__':
    main()

