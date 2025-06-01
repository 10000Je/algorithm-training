// no.1043: 거짓말 (G4)

#include <cstdio>
#include <vector>
using namespace std;

int find(int);
void _union(int, int);

vector<int> parent;

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    parent.assign(n+1, 0);
    for(int i=0; i<=n; i++)
        parent[i] = i;
    int k;
    scanf("%d", &k);
    vector<int> truth(k, 0);
    for(int i=0; i<k; i++) {
        scanf("%d", &truth[i]);
        _union(truth[0], truth[i]);
    }
    vector<vector<int>> parties(m);
    for(int i=0; i<m; i++) {
        int num;
        scanf("%d", &num);
        for(int j=0; j<num; j++) {
            int p;
            scanf("%d", &p);
            parties[i].push_back(p);
        }
        for(int x : parties[i]) {
            _union(x, parties[i][0]);
        }
    }
    int ret = 0;
    if(k == 0) {
        printf("%d\n", m);
        return 0;
    }
    int root = find(truth[0]);
    for(vector<int>& party : parties) {
        bool know = false;
        for(int x : party) {
            if(find(x) == root) {
                know = true;
                break;
            }
        }
        if(!know)
            ret++;
    }
    printf("%d\n", ret);
    return 0;
}

int find(int x) {
    if(x == parent[x])
        return x;
    parent[x] = find(parent[x]);
    return parent[x];
}

void _union(int a, int b) {
    int root_a = find(a);
    int root_b = find(b);
    parent[root_a] = root_b;
}
