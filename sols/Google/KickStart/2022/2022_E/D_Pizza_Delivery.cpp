/* Pizza Delivery
https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb0f5/0000000000ba86e6
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
const pair<int, int> dirs[4] = {{-1, 0}, {0, 1}, {0, -1}, {1, 0}};

LL f(pair<string, LL> params, LL c) {
    if (params.first == "+") return c + params.second;
    if (params.first == "-") return c - params.second;
    if (params.first == "*") return c * params.second;
    return (LL)floor(1. * c / params.second);
}

void solve(int test) {
    cout << "Case #" << test + 1 << ": ";

    int N, P, M, sr, sc, r, c, s;
    cin >> N >> P >> M >> sr >> sc;
    --sr, --sc;

    vector<pair<string, LL>> params(4);
    REP(i, 4) {
        cin >> params[i].first >> params[i].second;
    }

    map<int, pair<int, int>> pts;
    REP(i, P) {
        cin >> r >> c >> s;
        --r, --c;
        pts[r * N + c] = {i, s};
    }

    int ONE = (1 << P) - 1;
    LL res = -INF;
    vector<vector<vector<vector<LL>>>> dp(N, vector<vector<vector<LL>>>(N, vector<vector<LL>>(M + 2, vector<LL>(1 << P, -INF))));
    dp[sr][sc][0][0] = 0;

    priority_queue<array<LL, 5>> pq;
    pq.push({0, sr, sc, 0, 0});

    while (!pq.empty()) {
        auto [s, r, c, t, m] = pq.top();
        pq.pop();
        if (dp[r][c][t][m] < s) continue;

        if (m == ONE) res = max(res, s);

        if (pts.count(r * N + c)) {
            auto [b, add] = pts[r * N + c];
            if ((m >> b & 1) == 0) {
                LL nm = m | (1 << b);
                LL ns = s + add;
                if (ns > dp[r][c][t][nm]) {
                    dp[r][c][t][nm] = ns;
                    pq.push({ns, r, c, t, nm});
                }
            }
        }

        if (t >= M) continue;

        REP(i, 4) {
            auto [dr, dc] = dirs[i];
            LL nr = r + dr;
            LL nc = c + dc;
            if (nr < 0 || nr >= N || nc < 0 || nc >= N) continue;
            LL ns = f(params[i], s);
            if (ns > dp[nr][nc][t + 1][m]) {
                dp[nr][nc][t + 1][m] = ns;
                pq.push({ns, nr, nc, t + 1, m});
            }
        }
    }

    if (res > -INF) {
        cout << res << endl;
    } else {
        cout << "IMPOSSIBLE\n";
    }
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
