// no.2606: 바이러스 (S3)

#include <cstdio>
#include <vector>
#include <unordered_set>
using namespace std;

int dfs(vector<vector<bool>>, int=1, unordered_set<int>* visited=NULL);

int main() {
    int n;
    scanf("%d", &n);
    vector<vector<bool>> graph(n+1, vector<bool>(n+1, false));
    for(int i=1; i<=n; i++) {
        graph[i][i] = true;
    }
    int k;
    scanf("%d", &k);
    for(int i=0; i<k; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        graph[a][b] = true;
        graph[b][a] = true;
    }
    printf("%d\n", dfs(graph)-1);
    return 0;
}

int dfs(vector<vector<bool>> graph, int root, unordered_set<int>* visited) {
    int ret = 1;
    unordered_set<int> tmp;
    if(visited==NULL) {
        visited = &tmp;
    }
    visited->insert(root);
    for(int i=1; i<graph[root].size(); i++) {
        if(graph[root][i] && visited->count(i)==0) {
            ret += dfs(graph, i, visited);
        }
    }
    return ret;
}