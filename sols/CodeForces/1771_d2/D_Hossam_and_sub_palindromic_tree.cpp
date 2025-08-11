/* D. Hossam and (sub-)palindromic tree
https://codeforces.com/contest/1771/problem/D
 */

// g++-12 code.cpp

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

void solve(int test) {
    int N;
    cin >> N;

    string S;
    cin >> S;

    vector<pair<int, int>> edges;
    vector<vector<int>> adj(N, vector<int>());
    REP(i, N - 1) {
        int u, v;
        cin >> u >> v;
        --u, --v;
        adj[u].pb(v);
        adj[v].pb(u);
        edges.pb({u, v});
    }

    // dp[u][v] = max palin subseq on path u..v
    vector<vector<int>> dp(N, vector<int>(N, 0));
    REP(u, N) {
        dp[u][u] = 1;
    }

    deque<tuple<int, int, int, int>> queue;
    for (auto [u, v] : edges) {
        dp[u][v] = dp[v][u] = (S[u] == S[v]) ? 2 : 1;
        if (v > u) swap(u, v);
        queue.pb({u, v, v, u});
    }

    while (!queue.empty()) {
        auto [u, pu, v, pv] = queue.front();
        queue.pop_front();

        for (auto u2 : adj[u]) {
            if (dp[u2][v]) continue;
            dp[u2][v] = dp[v][u2] = (S[u2] == S[v]) ? 2 + dp[u][pv] : max(dp[u2][pv], dp[u][v]);
            queue.pb({u2, u, v, pv});
        }

        for (auto v2 : adj[v]) {
            if (dp[v2][u]) continue;
            dp[v2][u] = dp[u][v2] = (S[v2] == S[u]) ? 2 + dp[v][pu] : max(dp[v2][pu], dp[v][u]);
            queue.pb({v2, v, u, pu});
        }
    }

    int res = 1;
    REP(u, N) {
        REP(v, u) {
            res = max(res, dp[u][v]);
        }
    }

    cout << res << endl;
}

int T;
int main() {
    ios::sync_with_stdio(false);
    cin >> T;
    for (int t = 0; t < T; t++) {
        solve(t);
    }
    return 0;
}
