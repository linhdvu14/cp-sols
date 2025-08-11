/* E. Edge Reverse
https://codeforces.com/contest/1777/problem/E
 */

#pragma GCC optimize("O3")
#pragma GCC target("avx2")

#include <bits/stdc++.h>
using namespace std;

#define FOR(i, a, b) for (int i = (a), _##i = (b); i < _##i; ++i)
#define FORD(i, a, b) for (int i = (a), _##i = (b); i >= _##i; --i)
#define REP(i, a) for (int i = 0, _##i = (a); i < _##i; ++i)
#define REPD(i, n) for (int i = (n)-1; i >= 0; --i)
#define all(x) (x).begin(), (x).end()
#define pb push_back

typedef long long LL;

void solve() {
    int N, M;
    cin >> N >> M;

    vector<int> U(M), V(M), W(M);
    REP(i, M) {
        cin >> U[i] >> V[i] >> W[i];
        U[i]--, V[i]--;
    }

    auto is_ok = [&](int C) {
        vector<vector<int>> adj(N);
        REP(i, M) {
            adj[U[i]].pb(V[i]);
            if (W[i] <= C) adj[V[i]].pb(U[i]);
        }

        vector<int> tin(N, -1), root(N, -1), low(N), st;
        int cnt = 0, cc = 0;

        // tarjan scc
        auto dfs = [&](auto self, int u) -> void {
            st.pb(u);
            tin[u] = low[u] = cnt++;
            for (auto v : adj[u]) {
                if (tin[v] == -1) {
                    self(self, v);
                    low[u] = min(low[u], low[v]);
                } else if (root[v] == -1) {
                    low[u] = min(low[u], tin[v]);
                }
            }

            if (tin[u] == low[u]) {
                int v = -1;
                while (u != v) {
                    v = st.back();
                    st.pop_back();
                    root[v] = cc;
                }
                cc++;
            }
        };

        REP(u, N) {
            if (tin[u] == -1) dfs(dfs, u);
        }

        // should have 1 scc with indeg 0
        vector<int> deg(cc);
        REP(u, N) {
            for (auto v : adj[u]) {
                if (root[u] != root[v]) deg[root[v]]++;
            }
        }

        return count(deg.begin(), deg.end(), 0) == 1;
    };

    int res = -1, lo = 0, hi = 1E9;
    while (lo <= hi) {
        int mi = (lo + hi) / 2;
        if (is_ok(mi)) {
            res = mi;
            hi = mi - 1;
        } else {
            lo = mi + 1;
        }
    }

    cout << res << endl;
}

int T;
int main() {
    ios::sync_with_stdio(false);

    cin >> T;
    while (T--) {
        solve();
    }

    return 0;
}
