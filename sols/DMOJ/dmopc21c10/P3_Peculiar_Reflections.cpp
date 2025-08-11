/* DMOPC '21 Contest 10 P3 - Peculiar Reflections
https://dmoj.ca/problem/dmopc21c10p3
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

// 0 = U, 1 = D, 2 = L, 3 = R
// 0 = /, 1 =
array<int, 3> get_next(int r, int c, int v, int entering_dir) {
    switch (entering_dir) {
        case 0:
            if (!v) {
                return {r, c - 1, 3};
            }
            return {r, c + 1, 2};
        case 1:
            if (!v) {
                return {r, c + 1, 2};
            }
            return {r, c - 1, 3};
        case 2:
            if (!v) {
                return {r - 1, c, 1};
            }
            return {r + 1, c, 0};
        case 3:
            if (!v) {
                return {r + 1, c, 0};
            }
            return {r - 1, c, 1};
    }
    return {-1, -1, -1};
}

void solve() {
    int R, C;
    cin >> R >> C;

    string s;
    vector grid(R, vector<int>(C));
    REP(r, R) {
        cin >> s;
        REP(c, C) {
            grid[r][c] = (s[c] == '/') ? 0 : 1;
        }
    }

    vector<vector<vector<int>>> dist(4, vector<vector<int>>(R, vector<int>(C, R * C)));

    set<array<int, 4>> pq;
    pq.insert({0, 0, 0, 0});  // (cost, r, c, light entering direction)
    while (!pq.empty()) {
        // pop min ele
        auto [d, r, c, t] = *pq.begin();
        pq.erase(pq.begin());

        if (r == R && c == C - 1) {
            cout << d << endl;
            return;
        }

        if (!(0 <= r && r < R && 0 <= c && c < C) || dist[t][r][c] < R * C) {
            continue;
        }

        dist[t][r][c] = d;

        {
            auto [nr, nc, nt] = get_next(r, c, grid[r][c], t);
            pq.insert({d, nr, nc, nt});
        }

        {
            auto [nr, nc, nt] = get_next(r, c, grid[r][c] ^ 1, t);
            pq.insert({d + 1, nr, nc, nt});
        }
    }

    cout << -1 << endl;
}

int main() {
    ios::sync_with_stdio(false);
    solve();
    return 0;
}
