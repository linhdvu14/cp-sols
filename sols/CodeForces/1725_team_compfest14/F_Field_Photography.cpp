/*  F. Field Photography
https://codeforces.com/contest/1725/problem/F
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

// can move each seg by lsb(Z)
// all segs with length >= (1 << lsb(Z)) can be chosen
// choose max num of remaining segs by sliding window of size (1 << lsb(Z))
int main() {
    ios::sync_with_stdio(false);

    int N;
    cin >> N;

    vector<int> L(N), R(N);
    REP(i, N) {
        cin >> L[i] >> R[i];
        R[i]++;
    }

    // precompute for each lsb
    vector<int> f(30);
    REP(b, 30) {
        int w = 1 << b;

        vector<array<int, 2>> events;
        REP(i, N) {
            if (R[i] - L[i] >= w) {
                f[b]++;
            } else {
                int l = L[i] % w;
                int r = R[i] % w;
                if (l < r) {
                    events.pb({l, 1});
                    events.pb({r, -1});
                } else {
                    events.pb({0, 1});
                    events.pb({r, -1});
                    events.pb({l, 1});
                }
            }
        }
        sort(all(events));

        int mx = 0, cur = 0;
        for (auto [_, v] : events) {
            cur += v;
            mx = max(mx, cur);
        }

        f[b] += mx;
    }

    int Q, Z;
    cin >> Q;
    REP(i, Q) {
        cin >> Z;
        cout << f[__builtin_ctz(Z)] << "\n";
    }

    return 0;
}
