// no.13549: 숨바꼭질 3 (G5)

/*
 * 0-1 BFS 문제
 * 간선을 탐색할 때, x-1, x+1 의 순서가 결과에 영향을 준다.
 * 0-1 BFS 에서는 BFS와 달리, 이미 방문한 정점이 최단 거리가 되리란 보장이 없다.
 * 즉, 간선을 탐색할 때, 최단거리를 보장하게 끔 하거나, 아니면 갱신을 새롭게 해주는게 맞다.
 */

#include <cstdio>
#include <vector>
#include <deque>
using namespace std;

int bfs(int, int);

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    printf("%d\n", bfs(n, k));
    return 0;
}

int bfs(int start, int end) {
    deque<int> queue;
    vector<int> dist(100'001, -1);
    queue.push_back(start);
    dist[start] = 0;
    while(!queue.empty()) {
        int x = queue.front();
        queue.pop_front();
        vector<int> nodes = {x+1, x-1, 2*x};
        for(int node : nodes) {
            if(node < 0 || node > 100'000)
                continue;
            if(node == 2*x) {
                if(dist[node] != -1 && dist[x] >= dist[node])
                    continue;
                dist[node] = dist[x];
                queue.push_front(node);
            }
            else {
                if(dist[node] != -1 && dist[x]+1 >= dist[node])
                    continue;
                dist[node] = dist[x]+1;
                queue.push_back(node);
            }
        }
    }
    return dist[end];
}