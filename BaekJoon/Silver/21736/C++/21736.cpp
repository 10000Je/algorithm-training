// no.21736: 헌내기는 친구가 필요해 (S2)

#include <cstdio>
#include <vector>
#include <set>
using namespace std;

int dfs(vector<vector<char>>&, set<pair<int, int>>&, pair<int, int>);

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    vector<vector<char>> graph(n, vector<char>(m, 0));
    pair<int, int> root;
    for(int i=0; i<n; i++) {
        char tmp[601];
        scanf("%s", tmp);
        for(int j=0; j<m; j++) {
            graph[i][j] = tmp[j];
            if(tmp[j] == 'I') {
                root = make_pair(i, j);
            }
        }
    }
    set<pair<int, int>> visited;
    int ret = dfs(graph, visited, root);
    if(ret == 0) {
        printf("TT\n");
    }
    else {
        printf("%d\n", ret);
    }
    return 0;
}

int dfs(vector<vector<char>>& graph, set<pair<int, int>>& visited, pair<int, int> root) {
    visited.insert(root);
    vector<pair<int, int>> near;
    near.push_back(make_pair(root.first+1, root.second));
    near.push_back(make_pair(root.first-1, root.second));
    near.push_back(make_pair(root.first, root.second+1));
    near.push_back(make_pair(root.first, root.second-1));
    int ret = (graph[root.first][root.second] == 'P') ? 1 : 0;
    for(pair<int, int> tmp : near) {
        if(tmp.first<0 || tmp.first>=graph.size())
            continue;
        if(tmp.second<0 || tmp.second>=graph[tmp.first].size())
            continue;
        if(graph[tmp.first][tmp.second]=='X')
            continue;
        if(visited.count(tmp)!=0)
            continue;
        ret += dfs(graph, visited, tmp);
    }
    return ret;
}