/* G2. Magic Triples (Hard Version)
https://codeforces.com/contest/1822/problem/G2
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

unordered_map<int, int> SQRT;
void init() {
    FOR(b, 1001, 32001) {
        SQRT[b * b] = b;
    }
}

void solve() {
    int N;
    cin >> N;

    vector<int> A(N);
    map<int, int> cnt;
    REP(i, N) {
        cin >> A[i];
        cnt[A[i]]++;
    }
    sort(all(A));
    A.resize(unique(A.begin(), A.end()) - A.begin());

    LL res = 0;
    for (int a3 : A) {
        res += 1LL * cnt[a3] * (cnt[a3] - 1) * (cnt[a3] - 2);

        // b <= 1000
        FOR(b, 2, min(a3, 1000) + 1) {
            if (a3 % (b * b)) continue;
            res += 1LL * cnt[a3] * cnt[a3 / b] * cnt[a3 / b / b];
        }

        // b > 1000 -> a1 <= 1000
        for (int a1 : A) {
            if (a1 > 1000 || a1 > a3 / 4) break;
            if (a3 % a1) continue;
            int b2 = a3 / a1;
            if (!SQRT.count(b2)) continue;
            res += 1LL * cnt[a3] * cnt[a1] * cnt[a1 * SQRT[b2]];
        }
    }

    cout << res << endl;
}

int main() {
    ios::sync_with_stdio(false);
    init();

    int T;
    cin >> T;
    while (T--) {
        solve();
    }

    return 0;
}
