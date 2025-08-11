#pragma GCC optimize("O3")
#pragma GCC target("avx2,popcnt")

#include <bits/stdc++.h>
using namespace std;

#define FOR(i, a, b) for (int i = (a), _##i = (b); i < _##i; ++i)
#define FORD(i, a, b) for (int i = (a), _##i = (b); i >= _##i; --i)
#define REP(i, a) for (int i = 0, _##i = (a); i < _##i; ++i)
#define REPD(i, n) for (int i = (n)-1; i >= 0; --i)
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define eb emplace_back

typedef long long LL;
typedef unsigned long long ULL;

int n, m, x, y;
string s;

void solve() {
    cin >> n;
    cin >> s;
    set<pair<int, int>> black_holes;
    cin >> m;
    REP(i, m) {
        cin >> x >> y;
        black_holes.insert({x, y});
    }
    x = y = 0;
    auto move = [&](char dir) {
        if (dir == 'L')
            x--;
        else if (dir == 'R')
            x++;
        else if (dir == 'U')
            y++;
        else if (dir == 'D')
            y--;
    };

    REP(i, n) {
        move(s[i]);
        if (black_holes.count({x, y})) x = y = 0;
    }
    cout << x << " " << y << '\n';
}

int T;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> T;
    while (T--) solve();
    return 0;
}
