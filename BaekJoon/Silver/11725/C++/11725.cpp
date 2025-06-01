// no.11725: 트리의 부모 찾기 (S2)

#include <cstdio>
#include <vector>
using namespace std;

void dfs(vector<vector<int>>&, vector<int>&, int);

int main() {
    int n;
    scanf("%d", &n);
    vector<vector<int>> tree(n+1);
    for(int i=0; i<n-1; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        tree[a].push_back(b);
        tree[b].push_back(a);
    }
    vector<int> parent(n+1, -1);
    dfs(tree, parent, 1);
    for(int i=2; i<=n; i++) {
        printf("%d\n", parent[i]);
    }
    return 0;
}

void dfs(vector<vector<int>>& tree, vector<int>& parent, int root) {
    for(int node : tree[root]) {
        if(parent[node] != -1)
            continue;
        parent[node] = root;
        dfs(tree, parent, node);
    }
}
