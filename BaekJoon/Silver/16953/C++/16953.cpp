// no.16953: A -> B (S2)

#include <cstdio>
#include <vector>
#include <map>
#include <queue>
using namespace std;

int main() {
    int a, b;
    scanf("%d %d", &a, &b);
    queue<int> que;
    que.push(a);
    map<int, int> dist;
    dist[a] = 0;
    while(!que.empty()) {
        long long n = que.front();
        que.pop();
        vector<long long> nodes = {n*2, 10*n+1};
        for(long long node : nodes) {
            if(node<1 || node>int(1e9))
                continue;
            if(dist.count(node) != 0)
                continue;
            dist[node] = dist[n]+1;
            que.push(node);
        }
    }
    if(dist.count(b) != 0)
        printf("%d\n", dist[b]+1);
    else
        printf("%d\n", -1);
    return 0;
}