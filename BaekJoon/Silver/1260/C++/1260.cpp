// no.1260: DFS와 BFS (S2)

#include <cstdio>
#include <vector>
#include <unordered_set>
#include <deque>
using namespace std;

void dfs(vector<vector<int>>&, unordered_set<int>&, int);
void bfs(vector<vector<int>>&, int);

int main() {
    int n, m, v;
    scanf("%d %d %d", &n, &m, &v);
    vector<vector<int>> graph(n+1, vector<int>(n+1, 0));
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
    dfs(graph, visited, v);
    printf("\n");
    bfs(graph, v);
    return 0;
}

void dfs(vector<vector<int>>& graph, unordered_set<int>& visited, int root) {
    visited.insert(root);
    printf("%d ", root);
    for(int i=1; i<graph[root].size(); i++) {
        if(graph[root][i] && visited.count(i)==0)
            dfs(graph, visited, i);
    }
}

void bfs(vector<vector<int>>& graph, int root) {
    deque<int> que;
    unordered_set<int> visited;
    visited.insert(root);
    que.push_back(root);
    while(!que.empty()) {
        int cur = que.front();
        que.pop_front();
        printf("%d ", cur);
        for(int i=1; i<graph[cur].size(); i++) {
            if(graph[cur][i] && visited.count(i)==0) {
                que.push_back(i);
                visited.insert(i);
            }
        }
    }
    printf("\n");
}