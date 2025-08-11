/* D. Balancing Weapons
https://codeforces.com/contest/1814/problem/D
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
    int N, K;
    cin >> N >> K;

    vector<LL> F(N);
    REP(i, N) {
        cin >> F[i];
    }

    vector<LL> D(N);
    REP(i, N) {
        cin >> D[i];
    }

    int res = 0;
    REP(i, N) {
        LL p = F[i] * D[i];

        vector<array<LL, 3>> pos = {{p, i, 1}};
        REP(j, N) {
            if (j == i) continue;
            if (abs(D[j] * F[j] - p) <= K) pos.pb({1LL * D[j] * F[j], j, 1LL});
            LL lo = max(1LL, p / F[j]);
            REP(k, 2) {
                LL cand_p = lo * F[j];
                if (abs(p - cand_p) <= K) pos.pb({cand_p, j, lo == D[j] ? 1LL : 0LL});
                lo++;
            }
        }
        sort(all(pos));
        pos.resize(unique(all(pos)) - pos.begin());

        int l = 0, orig = 0, uniq = 0;
        vector<int> cnt(N);
        for (auto [p, i, o] : pos) {
            cnt[i]++;
            if (cnt[i] == 1) uniq++;
            orig += o;
            while (p - pos[l][0] > K) {
                auto [_, i1, o1] = pos[l];
                cnt[i1]--;
                if (!cnt[i1]) uniq--;
                orig -= o1;
                l++;
            }
            if (uniq == N) res = max(res, orig);
        }
    }

    cout << N - res << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;
    while (T--) {
        solve();
    }

    return 0;
}
