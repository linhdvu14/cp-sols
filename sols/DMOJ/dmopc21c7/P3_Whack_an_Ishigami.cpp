/* DMOPC ' 21 Contest 7 P3 - Whack-an-Ishigami
https://dmoj.ca/problem/dmopc21c7p3
*/

// g++ code.cpp
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

int N, M;
void solve() {
    cin >> N >> M;

    vector<int> S(N);
    REP(i, N) {
        cin >> S[i];
    }

    vector<vector<int>> adj(N, vector<int>());
    vector<vector<int>> rev_adj(N, vector<int>());
    vector<int> deg(N);
    int a, b;
    REP(i, M) {
        cin >> a >> b;
        --a, --b;
        adj[a].pb(b);
        rev_adj[b].pb(a);
        deg[a]++;
    }

    // toposort on reverse adj (i.e. pop nodes leading to nothing)
    // final order contains all nodes not leading into or inside cycle
    vector<int> topo;
    stack<int> st;
    REP(u, N) {
        if (!deg[u]) {
            st.push(u);
        }
    }

    while (!st.empty()) {
        int u = st.top();
        st.pop();
        topo.pb(u);
        for (int v : rev_adj[u]) {
            deg[v]--;
            if (!deg[v]) {
                st.push(v);
            }
        }
    }

    // push down flips using topo order
    reverse(all(topo));
    vector<int> flip(N);
    int res = 0;
    for (int u : topo) {
        if ((S[u] + flip[u]) & 1) {
            res++;
            flip[u]++;
        }
        for (int v : adj[u]) {
            flip[v] += flip[u];
        }
    }

    // now only all nodes not leading into or inside cycle handled
    // remaining nodes cannot be flipped
    // so check that orig state is 0
    REP(u, N) {
        if ((S[u] + flip[u]) & 1) {
            cout << -1 << endl;
            return;
        }
    }

    cout << res << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    solve();
    return 0;
}