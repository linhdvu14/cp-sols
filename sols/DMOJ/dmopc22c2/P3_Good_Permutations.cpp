/* DMOPC '22 Contest 2 P3 - Good Permutations
https://dmoj.ca/problem/dmopc22c2p3
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

void solve() {
    int N;
    cin >> N;

    vector<int> A(N);
    vector<int> pos(N + 1);
    REP(i, N) {
        cin >> A[i];
        pos[A[i]] = i;
    }

    vector<vector<int>> adj(N + 1, vector<int>());
    vector<int> deg(N + 1);
    vector<int> prime(N + 1, 1);

    FOR(d, 2, N / 2 + 1) {
        if (!prime[d]) continue;
        vector<pair<int, int>> dep;
        for (int d2 = d; d2 <= N; d2 += d) {
            dep.pb({pos[d2], d2});
            prime[d2] = 1;
        }
        sort(all(dep));
        REP(i, dep.size() - 1) {
            deg[dep[i + 1].second]++;
            adj[dep[i].second].pb(dep[i + 1].second);
        }
    }

    priority_queue<int> h;
    FOR(i, 1, N + 1) {
        if (!deg[i]) h.push(i);
    }

    while (!h.empty()) {
        int u = h.top();
        h.pop();
        cout << u << " ";
        for (int v : adj[u]) {
            deg[v]--;
            if (!deg[v]) h.push(v);
        }
    }

    cout << endl;
}

int main() {
    ios::sync_with_stdio(false);
    solve();
    return 0;
}
