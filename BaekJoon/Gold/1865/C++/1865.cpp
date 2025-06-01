// no.1865: 웜홀 (G3)

#include <cstdio>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;

bool belmanFord();
vector<tuple<int, int, int>> edges;
int n, m, w;

int main() {
    int tc;
    scanf("%d", &tc);
    for(int i=0; i<tc; i++) {
        edges.clear();
        scanf("%d %d %d", &n, &m, &w);
        for(int j=0; j<m; j++) {
            int s, e, t;
            scanf("%d %d %d", &s, &e, &t);
            edges.push_back(make_tuple(s, e, t));
            edges.push_back(make_tuple(e, s, t));
        }
        for(int j=0; j<w; j++) {
            int s, e, t;
            scanf("%d %d %d", &s, &e, &t);
            edges.push_back(make_tuple(s, e, -t));
        }
        if(belmanFord()) {
            printf("YES\n");
        }
        else {
            printf("NO\n");
        }
    }
    return 0;
}

bool belmanFord() {
    vector<int> dist(n+1, int(1e8));
    dist[1] = 0;
    for(int i=0; i<n-1; i++) {
        for(tuple<int, int, int> edge : edges) {
            int s = get<0>(edge), e = get<1>(edge), t = get<2>(edge);
            dist[e] = min(dist[e], dist[s]+t);
        }
    }
    for(tuple<int, int, int> edge : edges) {
        int s = get<0>(edge), e = get<1>(edge), t = get<2>(edge);
        if(dist[s]+t < dist[e]) {
           return true; 
        }
    }
    return false;
}