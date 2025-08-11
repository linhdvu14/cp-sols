/* C. Hossam and Trainees
https://codeforces.com/contest/1771/problem/C
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

vector<int> sieve(int N) {
    vector<int> primes;
    vector<int> lpf(N + 1);
    for (int i = 2; i <= N; i++) {
        if (!lpf[i]) {
            primes.pb(i);
            lpf[i] = i;
        }
        for (auto p : primes) {
            if (p * i > N || p > lpf[i]) break;
            lpf[p * i] = p;
        }
    }
    return primes;
}

vector<int> PRIMES = sieve(32000);

void solve() {
    int N, a;
    cin >> N;

    set<int> seen;
    string res = "NO";

    REP(i, N) {
        cin >> a;
        for (auto p : PRIMES) {
            if (p * p > a) break;
            if (!(a % p)) {
                if (seen.count(p)) {
                    res = "YES";
                    break;
                }
                seen.insert(p);
                while (!(a % p)) a /= p;
            }
        }
        if (a > 1) {
            if (seen.count(a)) res = "YES";
            seen.insert(a);
        }
    }

    cout << res << endl;
}

int main() {
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        solve();
    }
    return 0;
}
