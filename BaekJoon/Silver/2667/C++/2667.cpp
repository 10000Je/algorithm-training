// no. 2667: 단지번호붙이기 (S1)

#include <cstdio>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

void dfs(vector<vector<int>>&, set<pair<int, int>>&, pair<int, int>);

int main() {
    int n;
    scanf("%d", &n);
    vector<vector<int>> graph(n, vector<int>(n, 0));
    for(int i=0; i<n; i++) {
        char str[26];
        scanf("%s", str);
        for(int j=0; j<n; j++) {
            graph[i][j] = str[j]-'0';
        }
    }
    int ret = 0;
    vector<int> arr;
    set<pair<int, int>> visited;
    for(int r=0; r<n; r++) {
        for(int c=0; c<n; c++) {
            if(graph[r][c]==1) {
                ret++;
                dfs(graph, visited, make_pair(r, c));
                arr.push_back(visited.size());
                visited.clear();
            }
        }
    }
    sort(arr.begin(), arr.end());
    printf("%d\n", ret);
    for(int cnt : arr) {
        printf("%d\n", cnt);
    }
    return 0;
}

void dfs(vector<vector<int>>& graph, set<pair<int, int>>& visited, pair<int, int> root) {
    visited.insert(root);
    int r=root.first, c=root.second;
    graph[r][c] = 0;
    vector<pair<int, int>> nodes({make_pair(r-1, c), make_pair(r+1, c), make_pair(r, c-1), make_pair(r, c+1)});
    int n=graph.size(), m=graph[0].size();
    for(pair<int, int> node : nodes) {
        if(node.first<0 || node.first>=n)
            continue;
        if(node.second<0 || node.second>=m)
            continue;
        if(graph[node.first][node.second]==0)
            continue;
        if(visited.count(node)!=0)
            continue;
        dfs(graph, visited, node);
    }
}