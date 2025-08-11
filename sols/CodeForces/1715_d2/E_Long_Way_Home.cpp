/* E. Long Way Home
https://codeforces.com/contest/1715/problem/E
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

const LL INF = 1e15;

class LiChaoTree {
   private:
    const LL BITS = 30;
    LL N;
    vector<LL> tree;
    vector<LL> power;
    vector<pair<LL, LL>> lines;

   public:
    LiChaoTree(LL n) {
        power.resize(BITS + 1);
        power[0] = 1;
        for (LL j = 1; j <= BITS; j++) power[j] = power[j - 1] * 2;
        for (N = 0; true; N++) {
            if (power[N] >= n + 10) break;
        }
        tree.resize(power[N + 1] - 1, -1);
    }

    LL f(LL x, LL z) {
        if (z == -1) return INF;
        return lines[z].first * x + lines[z].second;
    }

    void addLine(LL m, LL c) {
        lines.push_back({m, c});

        function<void(LL, LL, LL, LL)> update = [&](LL z, LL l, LL r, LL cur) {
            LL mid = (l + r) / 2;
            LL l_lower = (f(l, z) > f(l, tree[cur]) ? tree[cur] : z);
            LL mid_lower = (f(mid, z) > f(mid, tree[cur]) ? tree[cur] : z);
            LL mid_upper = (mid_lower == tree[cur] ? z : tree[cur]);
            tree[cur] = mid_lower;
            if (l != r) {                    // not a leaf node
                if (l_lower != mid_lower) {  // intersection in [l..mid]
                    update(mid_upper, l, mid, 2 * cur + 1);
                } else {
                    update(mid_upper, mid + 1, r, 2 * cur + 2);
                }
            }
        };
        update((LL)lines.size() - 1, 0, power[N] - 1, 0);
    }

    // min query
    LL query(LL pos) {
        LL res = INF;
        LL cur = 0;
        LL l = 0, r = power[N] - 1;
        while (cur < (LL)tree.size()) {
            res = min(res, f(pos, tree[cur]));
            LL mid = (l + r) / 2;
            if (l <= pos && pos <= mid) {
                cur = 2 * cur + 1;
                r = mid;
            } else {
                cur = 2 * cur + 2;
                l = mid + 1;
            }
        }
        return res;
    }
};

// let f(k, v, u) = min dist v..u using at most k flights
//        g(k, u) = min dist 0..u using at most k flights s.t. the last flight ends at u
// --> want f(k, 0, u) for each u=0..n-1

// consider f(k, 0, u); if the last flight ends at v, then
// - f(k, 0, u) = g(k, v) + f(0, v, u)
// - g(k, v) = min_t f(k-1, 0, t) + (t-v)^2
// - t is picked to min f(k-1, 0, t) + t^2 - 2t*v
// --> graph for f(k, 0, u) contains only original edges and super edges w(0..v) = g(k, v)

void solve() {
    LL N, M, K;
    cin >> N >> M >> K;

    vector<pair<LL, LL>> adj[N];
    REP(i, M) {
        LL u, v, w;
        cin >> u >> v >> w;
        --u, --v;
        adj[u].emplace_back(v, w);
        adj[v].emplace_back(u, w);
    }

    vector<LL> f(N, INF);
    LiChaoTree lc = LiChaoTree(N);

    REP(k, K + 1) {
        set<array<LL, 2>> pq;
        pq.insert({0, 0});

        if (k > 0) {
            REP(u, N) {
                lc.addLine(-2 * u, f[u] + (LL)u * u);
            }
            REP(u, N) {
                LL w = lc.query(u) + (LL)u * u;
                pq.insert({w, u});
            }
        }

        while (!pq.empty()) {
            auto [d, u] = *pq.begin();
            pq.erase(pq.begin());
            if (d >= f[u]) continue;
            f[u] = d;
            for (auto [v, w] : adj[u]) {
                if (d + w >= f[v]) continue;
                pq.insert({d + w, v});
            }
        }
    }

    for (LL i = 0; i < N; i++) {
        cout << f[i] << " \n"[i == N - 1];
    }
}

int main() {
    ios::sync_with_stdio(false);
    solve();
    return 0;
}
