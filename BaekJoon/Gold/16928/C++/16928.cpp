// no.16928: 뱀과 사다리 게임 (G5)

#include <cstdio>
#include <vector>
#include <deque>
using namespace std;

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    vector<int> edge(101, -1);
    for(int i=0; i<n; i++) {
        int x, y;
        scanf("%d %d", &x, &y);
        edge[x] = y;
    }
    for(int i=0; i<m; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        edge[u] = v;
    }
    deque<int> que;
    vector<int> dist(101, -1);
    dist[1] = 0;
    que.push_back(1);
    while(!que.empty()) {
        int cur = que.front();
        que.pop_front();
        int dest = edge[cur];
        if(dest == -1) {
            for(int i=1; i<=6; i++) {
                if(cur+i > 100)
                    continue;
                if(dist[cur+i] != -1)
                    continue;
                dist[cur+i] = dist[cur]+1;
                if(edge[cur+i] != -1) {
                    que.push_front(cur+i);
                }
                else {
                    que.push_back(cur+i);
                }
            }
        }
        else {
            if(dist[dest] != -1)
                continue;
            dist[dest] = dist[cur];
            if(edge[dest] != -1) {
                que.push_front(dest);
            }
            else {
                que.push_back(dest);
            }
        }
    }
    printf("%d\n", dist[100]);
    return 0;
}