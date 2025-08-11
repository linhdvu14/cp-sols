/* Perfect Subarray
https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff43/00000000003381cb
 */
// g++ code.cpp

#include <bits/stdc++.h>
using namespace std;

#define FOR(i, a, b) for (int i = (a), _##i = (b); i < _##i; ++i)
#define FORD(i, a, b) for (int i = (a), _##i = (b); i >= _##i; --i)
#define REP(i, a) for (int i = 0, _##i = (a); i < _##i; ++i)
#define REPD(i, n) for (int i = (n)-1; i >= 0; --i)
#define pb push_back

typedef long long LL;

void solve(int test) {
    cout << "Case #" << test + 1 << ": ";

    int N;
    cin >> N;

    vector<int> A(N);
    int floor = 0;
    REP(i, N) {
        cin >> A[i];
        floor += abs(A[i]);
    }

    vector<int> count(2 * floor + 1);
    count[floor]++;

    int pref = 0;
    LL res = 0;
    REP(i, N) {
        pref += A[i];
        for (int j = 0; j * j <= floor + pref; j++) {
            res += count[floor + pref - j * j];
        }
        count[floor + pref]++;
    }

    cout << res << endl;
}

int T;
int main() {
    ios::sync_with_stdio(false);
    cin >> T;
    for (int test = 0; test < T; test++) {
        solve(test);
    }
    return 0;
}