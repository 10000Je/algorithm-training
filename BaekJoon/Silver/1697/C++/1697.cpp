// no.1697: 숨바꼭질 (S1)

#include <cstdio>
#include <map>
#include <queue>
#include <vector>
using namespace std;

int bfs(int, int);

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    printf("%d\n", bfs(n, k));
    return 0;
}

int bfs(int start, int end) {
    queue<int> que;
    que.push(start);
    map<int, int> dist;
    dist[start] = 0;
    while(!que.empty()) {
        int cur = que.front();
        que.pop();
        vector<int> nodes({cur-1, cur+1, 2*cur});
        for(int node : nodes) {
            if(node<0 || node>100'000)
                continue;
            if(dist.count(node)!=0)
                continue;
            dist[node] = dist[cur]+1;
            que.push(node);
        }
    }
    return dist[end];
}