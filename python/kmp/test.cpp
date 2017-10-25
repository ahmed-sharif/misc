#include <bits/stdc++.h>

using namespace std;

const int M = 1e6 * 20;
const int L = 0;
const int R = 1e6;

struct Node {
    Node *l, *r;
    int val;

    explicit Node(int x):
        l(nullptr),
        r(nullptr),
        val(x) { }

    Node():
        l(nullptr),
        r(nullptr),
        val(-1) { }
} pool[M];

int lastused = 0;

Node* getSome() {
    return pool + lastused++;
}

int get(Node *v, int l, int r, int at) {
    if (v == nullptr)
        return 0;

    if (l + 1 == r) {
        assert(at == l);
        return v->val;
    }

    int m = (l + r) / 2;
    if (at < m)
        return get(v->l, l, m, at);
    else
        return get(v->r, m, r, at);
}

Node* upd(Node *v, int l, int r, int at, int val) {
    auto res = getSome();

    if (v != nullptr)
        *res = *v;

    if (l + 1 == r) {
        assert(at == l);
        res->val = val;
        return res;
    }

    int m = (l + r) / 2;

    if (at < m) {
        res->l = upd(res->l, l, m, at, val);
    } else {
        res->r = upd(res->r, m, r, at, val);
    }

    return res;
}

Node* version[M];
int ans[M];

void test() {
    Node *root = getSome();

    int L = 0, R = 10;

    for (int i = 0; i < 10; ++i) {
        version[i] = root = upd(root, L, R, i, i);
        cout << "step " << i << ":\n";
        for (int j = 0; j < 10; ++j)
            cout << get(root, L, R, j) << " ";
        cout << "\n\n";
    }
}

void kill() {
    Node *empty = nullptr;

    int n;
    cin >> n;

    int m = 0; // cur length

    for (int i = 0; i < n; ++i) {
        char type;
        cin >> type;

        if (type == '-') {
            --m;
        } else {
            int x;
            cin >> x;
            --x;

            if (m == 0) {
                version[m] = upd(nullptr, L, R, x, 1);
            } else {
                int j = ans[m - 1];
                version[m] = upd(version[j], L, R, x, m + 1);
                ans[m] = get(version[j], L, R, x);
            }

            ++m;
        }

        cout << (m > 0 ? ans[m - 1] : 0) << "\n";

    }
}

int main() {
    kill();
    return 0;
}
