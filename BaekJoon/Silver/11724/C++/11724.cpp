// no.11724: 연결 요소의 개수 (S2)

#include <cstdio>
#include <vector>
#include <unordered_set>
using namespace std;

void dfs(vector<vector<int>>&, int, unordered_set<int>&);

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    vector<vector<int>> graph(n+1, vector(n+1, 0));
    for(int i=1; i<=n; i++) {
        graph[i][i] = 1;
    }
    for(int i=0; i<m; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        graph[a][b] = 1;
        graph[b][a] = 1;
    }
    unordered_set<int> visited;
    int cnt = 0;
    for(int i=1; i<=n; i++) {
        if(visited.count(i)==0) {
            cnt++;
            dfs(graph, i, visited);
        }
    }
    printf("%d\n", cnt);
    return 0;
}

void dfs(vector<vector<int>>& graph, int root, unordered_set<int>& visited) {
    visited.insert(root);
    for(int i=1; i<graph[root].size(); i++) {
        if(graph[root][i] && visited.count(i)==0)
            dfs(graph, i, visited);
    }
}