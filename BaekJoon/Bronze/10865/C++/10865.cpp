// no.10865: 친구 친구 (B3)

#include <cstdio>
#include <vector>
using namespace std;

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    vector<vector<int>> graph(n+1, vector<int>());
    for(int i=0; i<m; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    for(int i=1; i<=n; i++) {
        printf("%lu\n", graph[i].size());
    }
    return 0;
}