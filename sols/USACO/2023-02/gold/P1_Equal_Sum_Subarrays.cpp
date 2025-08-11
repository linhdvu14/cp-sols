/* Problem 1. Equal Sum Subarrays
 */

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

    vector<LL> A(N);
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }

    vector<tuple<LL, int, int>> B(N * (N + 1) / 2);
    int cnt = 0;
    for (int i = 0; i < N; i++) {
        LL s = 0;
        for (int j = i; j < N; j++) {
            s += A[j];
            B[cnt++] = {s, i, j};
        }
    }
    sort(all(B));

    vector<LL> res(N, LLONG_MAX);
    for (int i = 0; i < B.size() - 1; i++) {
        auto [s1, l1, r1] = B[i];
        auto [s2, l2, r2] = B[i + 1];
        FOR(j, l1, r1 + 1) {
            if (!(l2 <= j && j <= r2)) {
                res[j] = min(res[j], s2 - s1);
            }
        }
        FOR(j, l2, r2 + 1) {
            if (!(l1 <= j && j <= r1)) {
                res[j] = min(res[j], s2 - s1);
            }
        }
    }

    REP(i, N) {
        cout << res[i] << endl;
    }
}

int main() {
    ios::sync_with_stdio(false);
    solve();
    return 0;
}
