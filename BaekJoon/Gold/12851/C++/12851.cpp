// no.12851: 숨바꼭질 2 (G4)
/*
 * 큐에 푸시해주는 조건을 조심해야하는 문제
 * 단순하게 방문여부로 제한하면, k에 최단거리로 방문하는 경우의 수들을 전부 고려할 수 없음.
 * 예를들어 a -> b -> c -> d -> e 로 a에서 e로 가는 최단거리가 존재한다고 해보자.
 * 여기서 d로 최단거리로 가는 경우의 수가 2개가 존재한다고 해보자. 그때, 이미 방문한 정점이라고 큐에 푸시를 스킵하면
 * d로 가는 경우의 수 하나가 배제되어 버린다.
 * 따라서 조건은, 현재 이 경로를 통한 거리가 마찬가지로 최단거리인 경우로 제한해야한다.
*/

#include <cstdio>
#include <vector>
#include <queue>
using namespace std;

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    vector<int> dist(200'000, -1);
    queue<int> que;
    que.push(n);
    dist[n] = 0;
    int cnt = 1;

    while(!que.empty()) {
        int x = que.front();
        que.pop();
        vector<int> nodes = {x-1, x+1, 2*x};
        for(int node : nodes) {
            if(node < 0 || node >= 200'000)
                continue;
            if(node == k && dist[x]+1 <= dist[node])
                cnt++;
            if(dist[node] == -1 || dist[x]+1 <= dist[node]) {
                dist[node] = dist[x] + 1;
                que.push(node);
            }
        }
    }
    printf("%d\n", dist[k]);
    printf("%d\n", cnt);
    return 0;
}