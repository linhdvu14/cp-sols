/*
 D. Cut and Stick
https://codeforces.com/contest/1514/problem/D
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

// given a subset, let M = mx cnt element, R = remaining element
// subset is good iff cnt(M) + cnt(R) >= 2 * cnt(M) - 1, iff cnt(R) >= cnt(M) - 1
// optimal partitioning is (R's, cnt(R)+1 M's), (M), (M), ...
// --> need to find cnt(M) in all queried ranges

void solve() {
    int N, Q, l, r;
    cin >> N >> Q;

    vector<int> A(N);
    vector<vector<int>> pos(N, vector<int>());
    REP(i, N) {
        cin >> A[i];
        --A[i];
        pos[A[i]].pb(i);
    }

    mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
    while (Q--) {
        cin >> l >> r;
        --l, --r;
        int res = 1;
        REP(j, 40) {
            int a = A[l + rng() % (r - l + 1)];
            int cnt = upper_bound(all(pos[a]), r) - lower_bound(all(pos[a]), l);
            if (cnt > (r - l + 2) / 2) {
                int rem = r - l + 1 - cnt;
                res = cnt - rem;
                break;
            }
        }
        cout << res << endl;
    }
}

int main() {
    ios::sync_with_stdio(false);
    solve();
    return 0;
}