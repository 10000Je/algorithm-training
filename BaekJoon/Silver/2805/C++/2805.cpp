// no.2805: 나무 자르기 (S2)

#include <cstdio>
#include <vector>
using namespace std;

int bisect(vector<int>&, int, int, int);
long long cut(vector<int>&, int);

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    vector<int> tree;
    for(int i=0; i<n; i++) {
        int h;
        scanf("%d", &h);
        tree.push_back(h);
    }
    printf("%d\n", bisect(tree, m, 0, 1'000'000'000));
    return 0;
}

long long cut(vector<int>& tree, int h) {
    long long ret = 0;
    for(int t : tree) {
        if(t > h) {
            ret += (t-h);
        }
    }
    return ret;
}

int bisect(vector<int>& tree, int m, int left, int right) {
    if(left > right) {
        return right;
    }
    int mid = (left+right)/2;
    long long cur = cut(tree, mid);
    if(cur >= m) {
        return bisect(tree, m, mid+1, right);
    }
    else{
        return bisect(tree, m, left, mid-1);
    }
}
