// no.11404: 플로이드 (G4)

#include <cstdio>
#include <vector>
using namespace std;

int main() {
    int n, m;
    scanf("%d", &n);
    scanf("%d", &m);
    vector<vector<int>> dist(n+1, vector<int>(n+1, -1));
    for(int i=1; i<=n; i++) {
        dist[i][i] = 0;
    }
    for(int i=0; i<m; i++) {
        int a, b, c;
        scanf("%d %d %d", &a, &b, &c);
        if(dist[a][b] == -1 || c < dist[a][b])
            dist[a][b] = c;
    }
    for(int k=1; k<=n; k++) {
        for(int i=1; i<=n; i++) {
            for(int j=1; j<=n; j++) {
                if(dist[i][k] == -1 || dist[k][j] == -1)
                    continue;
                if(dist[i][j] == -1 || dist[i][k] + dist[k][j] < dist[i][j])
                    dist[i][j] = dist[i][k] + dist[k][j];
            }
        }
    }
    for(int i=1; i<=n; i++) {
        for(int j=1; j<=n; j++) {
            printf("%d ", dist[i][j] == -1 ? 0 : dist[i][j]);
        }
        printf("\n");
    }
    return 0;
}