#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    set<ll> st;
    map<ll, ll> cnt;

    ll Q;
    cin >> Q;
    for (ll i = 0; i < Q; i++) {
        ll num;
        cin >> num;
        if (num == 1) {
            ll x;
            cin >> x;
            st.insert(x);
            cnt[x] += 1;
        } else if (num == 2) {
            ll x, c;
            cin >> x >> c;
            cnt[x] -= min(c, cnt[x]);
            if (cnt[x] == 0) {
                st.erase(x);
            }
        } else {
            cout << *st.rbegin() - *st.begin() << endl;
        }
    }

    return 0;
}